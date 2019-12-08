from ..modules.administrator import Administrator
from ..modules.project import Project
from . import Dao


class DaoAuth(Dao):
    def __init__(self, module=None, session=None):
        super().__init__(module, session)

    def get_administrator_with_account(self, account):
        return self.session.query(Administrator).filter_by(account=account).first()

    def get_project_with_name_auth_code(self, name, auth_code):
        return self.session.query(Project).filter(Project.name == name, Project.auth_code == auth_code).first()

