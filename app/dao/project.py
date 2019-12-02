from ..lib.database import DB
from ..modules.project import Project
from . import Dao


class DaoProject(Dao):
    def __init__(self, module=Project, session=None):
        super().__init__(module, session)

    @DB.session
    def get_project(self, _id, **kwargs):
        return self.session.query(self.module).filter_by(id=_id).first()

