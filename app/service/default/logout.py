from ...lib.cache import Cache
from .. import Service


class ServiceDefaultLogout(Service):
    def __init__(self):
        super().__init__()

    def auth_verify(self, account):
        return Cache.memory.get("ray-iam-auth", {}).pop(account, None)

