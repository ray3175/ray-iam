from ..modules.mail import Mail
from . import Dao


class DaoMail(Dao):
    def __init__(self, module=Mail):
        super().__init__(module)


