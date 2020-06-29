from ..lib.cache.redis import CacheRedis
from ..lib.database.session import Session
from . import Service
from .administrator import ServiceAdministrator
from .project import ServiceProject


class ServiceAuth(Service):
    cache_redis = CacheRedis()

    def __init__(self):
        super().__init__()

    def ray_iam_auth(self, account, password):
        return ServiceAdministrator().ray_iam_auth(account, password)

    def ray_iam_max_auth(self, account, auth=99):
        return ServiceAdministrator().ray_iam_max_auth(account, auth)

    @Session.transaction(auto_commit=False)
    def project_iam_auth_from_DB(self, name, auth_code):
        return (project:=ServiceProject().project_iam_auth(name, auth_code)) and project()

    @cache_redis.cache("project", "name")
    def project_iam_auth(self, name, auth_code):
        return self.project_iam_auth_from_DB(name, auth_code)
