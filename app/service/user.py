from ..lib.database.session import Session
from ..dao.user import DaoUser
from . import Service


class ServiceUser(Service):
    def __init__(self, dao=DaoUser):
        super().__init__(dao)

    @Session.transaction(auto_commit=False)
    def get_user(self, _id):
        return (user:=self.dao.get_user(_id)) and user()

    @Session.transaction(auto_commit=False)
    def get_user_with_account(self, account, xy=True):
        return (user:=self.dao.get_user_with_account(account, xy)) and user(add_column=["person", "phone", "mail", "we_chat_user"])


