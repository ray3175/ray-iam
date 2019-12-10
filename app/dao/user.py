from ..modules.user import User
from . import Dao


class DaoUser(Dao):
    def __init__(self, module=User, session=None):
        super().__init__(module, session)

    def get_user(self, _id):
        return self.session.query(self.module).filter_by(id=_id).first()

    def get_user_with_account(self, account, xy=True):
        return self.session.query(self.module).filter(self.module.account == account, self.module.xy == xy).first()

