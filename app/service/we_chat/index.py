import requests
from xy.exception import XYException, XYInfo
from ...config import AppConfig
from ...lib.cache.redis import CacheRedis
from ...common.hash import RayIamHash
from .. import Service
from .user import ServiceWeChatUser


class ServiceWeChat(Service):
    cache_redis = CacheRedis()

    def __init__(self):
        super().__init__()
        self.__token_config = AppConfig().app["token-config"]
        self.__we_chat_config = AppConfig()["third-party-platform"]["we_chat"]
        self.__app_id = self.__we_chat_config["appid"]
        self.__secret = self.__we_chat_config["secret"]
        self.__api = self.__we_chat_config["api"]

    @staticmethod
    def new_token(openid, session_key):
        return RayIamHash(salt=session_key).encrypt(openid)

    def we_chat_api_code2Session(self, code):
        config = self.__api["code2Session"]
        url, grant_type = config["url"], config["grant_type"]
        try:
            rsp = requests.get(url, params={"appid": self.__app_id, "secret": self.__secret, "js_code": code, "grant_type": grant_type})
            data = rsp.json()
        except Exception as e:
            raise XYException(e)
        return data

    @cache_redis.cache("we_chat", "token")
    def get_we_chat_user_with_openid_priority_cache_redis(self, token, call=None):
        if callable(call):
            call = call()
        return call

    def get_user_with_we_chat_code(self, code):
        rsp_json = self.we_chat_api_code2Session(code)
        openid = rsp_json.get("openid")
        session_key = rsp_json.get("session_key")
        token = self.new_token(openid, session_key)
        if we_chat_user:=self.get_we_chat_user_with_openid_priority_cache_redis(token, lambda : ServiceWeChatUser().get_we_chat_user_with_openid(openid)):
            we_chat_user.update({self.__token_config["key"]: token})
        return we_chat_user

    def add_user_from_we_chat_code(self, code, account, password, id_card, name, sex, birth_date, birth_place, native_place, nationality, phone, mail):
        rsp_json = self.we_chat_api_code2Session(code)
        if not (openid:=rsp_json.get("openid")):
            raise XYInfo("未获取到微信openid！")
        if ServiceWeChatUser().get_user_with_account(account):
            raise XYInfo("该账号已存在！")
        return ServiceWeChatUser().add_we_chat_user_with_openid(openid, account, password, id_card, name, sex, birth_date, birth_place, native_place, nationality, phone, mail)

    def bind_user_from_we_chat_code(self, code, account, password):
        rsp_json = self.we_chat_api_code2Session(code)
        if not (openid:=rsp_json.get("openid")):
            raise XYInfo("未获取到微信openid！")
        if not (we_chat_user:=ServiceWeChatUser().get_user_with_account(account, True)):
            raise XYInfo("该账号不存在或已失效！")
        if we_chat_user["password"] != password:
            raise XYInfo("密码不正确！")
        person_id = we_chat_user["person_id"]
        return ServiceWeChatUser().add_we_chat_user(openid, person_id)

