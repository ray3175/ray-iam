from ..modules.administrator import Administrator
from . import Dao


class DaoAdministrator(Dao):
    def __init__(self, module=Administrator, session=None):
        super().__init__(module, session)

    def get_administrator(self, _id):
        return self.session.query(self.module).filter_by(id=_id).first()

    def get_administrator_with_account(self, account):
        return self.session.query(Administrator).filter_by(account=account).first()

