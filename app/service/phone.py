from ..lib.database import DB
from ..dao.phone import DaoPhone
from . import Service


class ServicePhone(Service):
    def __init__(self, dao=DaoPhone):
        super().__init__(dao)


