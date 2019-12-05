from ...dao import Dao
from .. import Service
from ..auth import ServiceAuth


class ServiceDefaultLogin(Service):
    def __init__(self, dao=Dao):
        super().__init__(dao)

    def auth_verify(self, account, password):
        return ServiceAuth().ray_iam_auth(account, password)
