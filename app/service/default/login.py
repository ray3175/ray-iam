from .. import Service
from ..auth import ServiceAuth


class ServiceDefaultLogin(Service):
    def __init__(self):
        super().__init__()

    def auth_verify(self, account, password):
        return ServiceAuth().ray_iam_auth(account, password)
