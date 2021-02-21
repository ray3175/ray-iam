from ..lib.cache.redis import CacheRedis
from . import Service
from .administrator import ServiceAdministrator
from .project import ServiceProject


class ServiceAuth(Service):
    def __init__(self):
        super().__init__()

    def ray_sso_auth(self, account, password):
        return ServiceAdministrator().ray_sso_auth(account, password)

    def ray_sso_max_auth(self, account, auth=99):
        return ServiceAdministrator().ray_sso_max_auth(account, auth)

    def project_sso_auth_from_DB(self, name, auth_code):
        return (project:=ServiceProject().project_sso_auth(name, auth_code)) and project()

    @CacheRedis().cache("project", "name")
    def project_sso_auth(self, name, auth_code):
        return self.project_sso_auth_from_DB(name, auth_code)
