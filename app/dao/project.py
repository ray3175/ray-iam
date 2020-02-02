from ..modules.project import Project
from . import Dao


class DaoProject(Dao):
    def __init__(self, module=Project, session=None):
        super().__init__(module, session)

    def get_project(self, _id):
        return self.session.query(self.module).filter_by(id=_id).first()

    def get_project_with_name_auth_code(self, name, auth_code):
        return self.session.query(Project).filter(Project.name == name, Project.auth_code == auth_code).first()
