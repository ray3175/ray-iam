from threading import Thread
import requests
from ...lib.cache import Cache
from ...common.hash import RayIamHash
from ...dao import Dao
from .. import Service
from ..user import ServiceUser
from ..project import ServiceProject


class ServiceIamAuth(Service):
    def __init__(self, dao=Dao):
        super().__init__(dao)

    def __defined_http_params_with_project(self, hash_account, url_key):
        self.__project = ServiceProject().get({"active": True})
        self.__hash_account = hash_account
        self.__url_key = url_key
        return True

    def __new_batch_thread_to_http_request_with_project(self, user=None):
        t_pool = list()
        _json = dict(hash_account=self.__hash_account)
        if isinstance(user, dict):
            _json.update({"user": user})
        for project in self.__project:
            if project[self.__url_key]:
                t_pool.append(Thread(target=lambda : requests.post(project[self.__url_key], json=_json)))
        for i in t_pool:
            i.start()
        return t_pool

    @Cache.cache_redis("auth", "hash_account")
    def get_user_with_hash_account(self, hash_account, call=None):
        if callable(call):
            call = call()
        return call

    def iam_auth(self, account, password):
        hash_account = RayIamHash(salt=password).encrypt(account)
        return hash_account if (user:=self.get_user_with_hash_account(hash_account, lambda : user if (user:=ServiceUser().get_user_with_account(account)) and user["password"]==password else None)) else user

    def active_hash_account_to_all_project(self, hash_account, user):
        self.__defined_http_params_with_project(hash_account, "login_url")
        self.__new_batch_thread_to_http_request_with_project(user)
        return True

    def logout_hash_account_to_all_project(self, hash_account):
        self.delete_hash_account_from_auth_redis(hash_account)
        self.__defined_http_params_with_project(hash_account, "logout_url")
        self.__new_batch_thread_to_http_request_with_project()
        return True

    def delete_hash_account_from_auth_redis(self, hash_account):
        return Cache.auth_redis.delete(hash_account)


