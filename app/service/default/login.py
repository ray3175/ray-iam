from xy.common.global_data import GlobalData
from ...dao import transaction
from ...dao.default.login import DaoDefaultLogin


class ServiceDefaultLogin:
    global_data = GlobalData()

    @classmethod
    @transaction(auto_commit=False)
    def auth_verify(cls, user, password, **kwargs):
        if not ((administrator:=DaoDefaultLogin.get_administrator_with_account(user, **kwargs)) and administrator.password == password):
            return None
        cls.global_data["ray-iam-auth"][user] = password
        return True
