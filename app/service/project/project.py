from ...lib.database import DB
from ...dao.project.project import DaoProjectProject
from .. import Service


class ServiceProjectProject(Service):
    def __init__(self):
        super().__init__(DaoProjectProject)


