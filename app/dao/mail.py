from ..modules.mail import Mail
from . import Dao


class DaoMail(Dao):
    def __init__(self, module=Mail, session=None):
        super().__init__(module, session)


