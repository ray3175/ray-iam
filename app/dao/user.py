from ..modules.user import User
from . import Dao


class DaoUser(Dao):
    def __init__(self, module=User):
        super().__init__(module)

    def get_user(self, _id):
        return self.session.query(self.module).filter_by(id=_id).first()

    def get_user_with_account(self, account, xy=None):
        condition = [self.module.account == account]
        if xy is not None:
            condition.append(self.module.xy == xy)
        return self.session.query(self.module).filter(*condition).first()

