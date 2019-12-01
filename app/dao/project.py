from ..lib.database import DB
from ..modules.project import Project
from . import Dao


class DaoProject(Dao):
    def __init__(self):
        super().__init__(Project)

    @DB.session
    def get_project(self, _id, **kwargs):
        return self.session.query(self.module).filter_by(id=_id).first()

