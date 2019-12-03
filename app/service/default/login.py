from ...dao import Dao
from .. import Service
from ..auth import ServiceAuth


class ServiceDefaultLogin(Service):
    def __init__(self, dao=Dao):
        super().__init__(dao)

    def auth_verify(self, user, password):
        return ServiceAuth().ray_iam_auth(user, password)
