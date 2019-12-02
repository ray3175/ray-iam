from ..lib.database import DB
from ..dao.mail import DaoMail
from . import Service


class ServiceMail(Service):
    def __init__(self, dao=DaoMail):
        super().__init__(dao)


