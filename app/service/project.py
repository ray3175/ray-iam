from ..lib.database import DB
from ..dao.project import DaoProject
from . import Service


class ServiceProject(Service):
    def __init__(self, dao=DaoProject):
        super().__init__(dao)

    @DB.transaction(auto_commit=False)
    def get_project(self, _id, **kwargs):
        return (project:=self.dao.get_project(_id)) and project.dict()


