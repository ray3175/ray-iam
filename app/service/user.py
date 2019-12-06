from ..lib.database import DB
from ..dao.user import DaoUser
from . import Service


class ServiceUser(Service):
    def __init__(self, dao=DaoUser):
        super().__init__(dao)

    @DB.transaction(auto_commit=False)
    def get_user(self, _id, **kwargs):
        return (user:=self.dao.get_user(_id)) and user()

    @DB.transaction(auto_commit=False)
    def get_user_with_account(self, account, **kwargs):
        return (user:=self.dao.get_user_with_account(account)) and user()


