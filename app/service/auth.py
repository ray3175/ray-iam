from ..lib.database import DB
from ..lib.cache import Cache
from ..dao.auth import DaoAuth
from . import Service


class ServiceAuth(Service):
    def __init__(self, dao=DaoAuth):
        super().__init__(dao)

    @DB.transaction(auto_commit=False)
    def get_administrator_password_with_user(self, account, **kwargs):
        return (administrator:=self.dao.get_administrator_with_account(account)) and administrator.password

    @Cache.cache_memory("ray-iam-auth", "account")
    def get_administrator_password_with_user_priority_cache_memory(self, account):
        return self.get_administrator_password_with_user(account)

    def ray_iam_auth(self, account, password):
        return (_password:=self.get_administrator_password_with_user_priority_cache_memory(account)) and _password == password

    @DB.transaction(auto_commit=False)
    def project_iam_auth(self, name, auth_code, **kwargs):
        return self.dao.get_project_with_name_auth_code(name, auth_code)
