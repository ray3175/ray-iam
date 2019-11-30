from ...modules.project import Project
from .. import Dao


class DaoProjectProject(Dao):
    def __init__(self):
        super().__init__(Project)

