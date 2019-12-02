from xy.common.global_data import GlobalData
from ..dao import Dao
from . import Service


class ServiceAuth(Service):
    global_data = GlobalData()

    def __init__(self, dao=Dao):
        super().__init__(dao)

    def ray_iam_auth(self, user, password):
        return password and password == self.global_data["ray-iam-auth"].get(user)
