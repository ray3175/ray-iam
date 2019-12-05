from ..lib.cache import Cache
from ..dao.auth import DaoAuth
from . import Service


class ServiceAuth(Service):
    def __init__(self, dao=DaoAuth):
        super().__init__(dao)

    @Cache.cache_memory("ray-iam-auth", "account")
    def get_administrator_password_with_user(self, account):
        return (administrator:=self.dao.get_administrator_with_account(account)) and administrator.password

    def ray_iam_auth(self, account, password):
        return (_password:=self.get_administrator_password_with_user(account)) and _password == password
