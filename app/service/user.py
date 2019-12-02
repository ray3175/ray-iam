from ..lib.cache import Cache
from ..lib.database import DB
from ..dao.user import DaoUser
from .person import ServicePerson
from .phone import ServicePhone
from .mail import ServiceMail
from . import Service


class ServiceUser(Service):
    def __init__(self, dao=DaoUser):
        super().__init__(dao)

    @DB.transaction(auto_commit=False)
    def get_user(self, _id, **kwargs):
        return (user:=self.dao.get_user(_id)) and user.dict()

    @Cache.cache_redis("user", "account")
    @DB.transaction(auto_commit=False)
    def get_user_with_account(self, account, **kwargs):
        return (user:=self.dao.get_user_with_account(account)) and user.dict()

    @DB.transaction
    def add_user(self, account, password, id_card, name, sex, birth_date, birth_place, native_place, nationality, phone, mail, **kwargs):
        person_id = None
        if id_card:
            person_id = ServicePerson().add_person(id_card, name, sex, birth_date, birth_place, native_place, nationality, **kwargs)["id"]
            if phone:
                ServicePhone().add({"phone": phone, "person_id": person_id}, **kwargs)
            if mail:
                ServiceMail().add({"mail": mail, "person_id": person_id}, **kwargs)
        return self.dao.add({"account": account, "password": password, "person_id": person_id})


