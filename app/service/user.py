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
    def get_user_with_account(self, account, xy=True, **kwargs):
        return (user:=self.dao.get_user_with_account(account, xy)) and user(add_column=["person", "phone", "mail", "we_chat_user"])

    @DB.transaction(auto_commit=False)
    def get_all_user_del_password(self, condition=None, offset=None, limit=None, reverse=False, condition_like=False, **kwargs):
        return [user(add_column=["person", "phone", "mail", "we_chat_user"], del_column=["password"]) for user in self.dao.get(condition, offset, limit, reverse, condition_like)]


