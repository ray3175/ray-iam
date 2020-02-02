from ..lib.database import DB
from ..lib.cache import Cache
from ..dao.administrator import DaoAdministrator
from . import Service


class ServiceAdministrator(Service):
    def __init__(self, dao=DaoAdministrator):
        super().__init__(dao)

    @DB.transaction(auto_commit=False)
    def get_administrator_password_with_user(self, account, **kwargs):
        return (administrator:=self.dao.get_administrator_with_account(account)) and administrator.password

    @Cache.cache_memory("ray-iam-auth", "account")
    def get_administrator_password_with_user_priority_cache_memory(self, account):
        return self.get_administrator_password_with_user(account)

    def ray_iam_auth(self, account, password):
        return (_password:=self.get_administrator_password_with_user_priority_cache_memory(account)) and _password == password

