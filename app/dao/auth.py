from ..modules.administrator import Administrator
from . import Dao


class DaoAuth(Dao):
    def __init__(self, module=None, session=None):
        super().__init__(module, session)

    def get_administrator_with_account(self, account):
        return self.session.query(Administrator).filter_by(account=account).first()

