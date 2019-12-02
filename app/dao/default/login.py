from ...lib.database import DB
from ...modules.administrator import Administrator
from .. import Dao


class DaoDefaultLogin(Dao):
    def __init__(self, module=None, session=None):
        super().__init__(module, session)

    @DB.session
    def get_administrator_with_account(self, account, **kwargs):
        return self.session.query(Administrator).filter_by(account=account).first()

