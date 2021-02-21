from ..lib.database.session import Session
from ..dao.project import DaoProject
from . import Service


class ServiceProject(Service):
    def __init__(self, dao=DaoProject):
        super().__init__(dao)

    @Session.transaction(auto_commit=False)
    def get_project(self, _id):
        return (project:=self.dao.get_project(_id)) and project()

    @Session.transaction(auto_commit=False)
    def project_sso_auth(self, name, auth_code):
        return self.dao.get_project_with_name_auth_code(name, auth_code)

