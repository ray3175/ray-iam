from ..lib.database import DB
from ..modules.phone import Phone
from . import Dao


class DaoPhone(Dao):
    def __init__(self, module=Phone, session=None):
        super().__init__(module, session)


