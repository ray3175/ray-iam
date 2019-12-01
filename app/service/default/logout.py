from xy.common.global_data import GlobalData
from .. import Service


class ServiceDefaultLogout(Service):
    global_data = GlobalData()

    def __init__(self):
        super().__init__()

    def auth_verify(self, user):
        return self.global_data["ray-iam-auth"].pop(user, None)

