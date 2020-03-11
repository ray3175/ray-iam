import requests
from xy.exception import XYException
from ...config import AppConfig
from ...lib.database import DB
from .. import Service


class ServiceWeChart(Service):
    def __init__(self):
        super().__init__()
        self.__we_chat_config = AppConfig()["we_chat"]
        self.__app_id = self.__we_chat_config["appid"]
        self.__secret = self.__we_chat_config["secret"]
        self.__api = self.__we_chat_config["api"]

    def code2Session(self, code):
        config = self.__api["code2Session"]
        url, grant_type = config["url"], config["grant_type"]
        try:
            rsp = requests.get(url, params={"appid": self.__app_id, "secret": self.__secret, "js_code": code, "grant_type": grant_type})
            data = rsp.json()
        except Exception as e:
            raise XYException(e)
        openid = data.get("openid")
        session_key = data.get("session_key")
        print(openid)
        print(session_key)
        return None

