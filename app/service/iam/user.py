from ...lib.database import DB
from .. import Service
from ..user import ServiceUser
from ..person import ServicePerson
from ..phone import ServicePhone
from ..mail import ServiceMail


class ServiceIamUser(Service):
    def __init__(self):
        super().__init__()

    @DB.transaction
    def add_user(self, account, password, id_card, name, sex, birth_date, birth_place, native_place, nationality, phone, mail, **kwargs):
        person_id = None
        if id_card:
            person_id = person[0]["id"] if (person:=ServicePerson().get({"id_card": id_card}, **kwargs)) else ServicePerson().add_person(id_card, name, sex, birth_date, birth_place, native_place, nationality, **kwargs)["id"]
        if person_id:
            if phone:
                ServicePhone().add({"phone": phone, "person_id": person_id}, **kwargs)
            if mail:
                ServiceMail().add({"mail": mail, "person_id": person_id}, **kwargs)
        return ServiceUser().add({"account": account, "password": password, "person_id": person_id}, **kwargs)


