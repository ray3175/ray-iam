from ..lib.database.session import Session
from ..lib.cache.memory import CacheMemory
from ..dao.administrator import DaoAdministrator
from . import Service


class ServiceAdministrator(Service):
    def __init__(self, dao=DaoAdministrator):
        super().__init__(dao)

    @Session.transaction(auto_commit=False)
    def get_administrator(self, _id):
        return (administrator:=self.dao.get_administrator(_id)) and administrator()

    @Session.transaction(auto_commit=False)
    def get_administrator_with_account(self, account):
        return (administrator:=self.dao.get_administrator_with_account(account)) and administrator()

    @CacheMemory().cache("ray-iam-administrator", "account")
    def get_administrator_with_user_priority_cache_memory(self, account):
        return self.get_administrator_with_account(account)

    def ray_iam_auth(self, account, password):
        return (administrator:=self.get_administrator_with_user_priority_cache_memory(account)) and administrator["password"] == password

    def ray_iam_max_auth(self, account, auth=99):
        return (administrator:=self.get_administrator_with_user_priority_cache_memory(account)) and administrator["auth"] >= auth


