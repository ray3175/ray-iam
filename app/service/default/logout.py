from ...lib.cache.memory import CacheMemory
from .. import Service


class ServiceDefaultLogout(Service):
    def __init__(self):
        super().__init__()

    def auth_verify(self, account):
        return CacheMemory().memory.get("ray-sso-administrator", {}).pop(account, None)

