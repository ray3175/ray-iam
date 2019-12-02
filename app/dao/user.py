from ..lib.database import DB
from ..modules.user import User
from . import Dao


class DaoUser(Dao):
    def __init__(self, module=User, session=None):
        super().__init__(module, session)

    @DB.session
    def get_user(self, _id, **kwargs):
        return self.session.query(self.module).filter_by(id=_id).first()

    @DB.session
    def get_user_with_account(self, account, **kwargs):
        return self.session.query(self.module).filter_by(account=account)


