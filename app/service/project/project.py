from ...lib.database import DB
from ...dao.project import DaoProject
from .. import Service


class ServiceProjectProject(Service):
    def __init__(self):
        super().__init__(DaoProject)

    @DB.transaction(auto_commit=False)
    def get_project(self, _id, **kwargs):
        return (project:=self.dao.get_project(_id, **kwargs)) and project.dict()


