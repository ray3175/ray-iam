from xy.common.global_data import GlobalData
from ...dao import Dao
from .. import Service


class ServiceDefaultLogout(Service):
    global_data = GlobalData()

    def __init__(self, dao=Dao):
        super().__init__(dao)

    def auth_verify(self, user):
        return self.global_data["ray-iam-auth"].pop(user, None)

