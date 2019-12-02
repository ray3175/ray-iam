from xy.common.global_data import GlobalData
from ...lib.database import DB
from ...dao import Dao
from ...dao.default.login import DaoDefaultLogin
from .. import Service


class ServiceDefaultLogin(Service):
    global_data = GlobalData()

    def __init__(self, dao=Dao):
        super().__init__(dao)

    @DB.transaction(auto_commit=False)
    def auth_verify(self, user, password, **kwargs):
        if not ((administrator:=DaoDefaultLogin(session=self.dao.session).get_administrator_with_account(user)) and administrator.password == password):
            return None
        self.global_data["ray-iam-auth"][user] = password
        return True
