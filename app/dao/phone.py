from ..modules.phone import Phone
from . import Dao


class DaoPhone(Dao):
    def __init__(self, module=Phone):
        super().__init__(module)


