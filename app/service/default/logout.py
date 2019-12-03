from ...lib.cache import Cache
from ...dao import Dao
from .. import Service


class ServiceDefaultLogout(Service):
    def __init__(self, dao=Dao):
        super().__init__(dao)

    def auth_verify(self, user):
        return Cache.memory.get("ray-iam-auth", {}).pop(user, None)

