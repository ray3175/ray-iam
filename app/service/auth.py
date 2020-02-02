from ..lib.database import DB
from . import Service
from .administrator import ServiceAdministrator
from .project import ServiceProject


class ServiceAuth(Service):
    def __init__(self):
        super().__init__()

    def ray_iam_auth(self, account, password):
        return ServiceAdministrator().ray_iam_auth(account, password)

    @DB.transaction(auto_commit=False)
    def project_iam_auth(self, name, auth_code, **kwargs):
        return ServiceProject().project_iam_auth(name, auth_code, **kwargs)
