from ...common.hash import RayIamHash
from ...dao import Dao
from .. import Service
from ..user import ServiceUser


class ServiceIamAuth(Service):
    def __init__(self, dao=Dao):
        super().__init__(dao)

    def _hash_password(self, password):
        return RayIamHash().encrypt(password)

    def iam_auth(self, account, password):
        user = ServiceUser().get_user_with_account_with_cache_priority(account)
        return self._hash_password(password) if user and user["password"] == password else None
