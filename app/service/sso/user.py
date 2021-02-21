from xy.utils.time import Time
from ...lib.database.session import Session
from .. import Service
from ..user import ServiceUser
from ..person import ServicePerson
from ..phone import ServicePhone
from ..mail import ServiceMail


class ServiceSSOUser(Service):
    def __init__(self):
        super().__init__()

    @Session.transaction
    def add_user(self, account, password, id_card, name, sex, birth_date, birth_place, native_place, nationality, phone, mail):
        person_id = None
        if id_card:
            person_id = person.id if (person:=ServicePerson().get_person_obj_with_id_card(id_card)) else ServicePerson().add_person(id_card, name, sex, birth_date, birth_place, native_place, nationality)["id"]
        if person_id:
            if phone:
                ServicePhone().add({"phone": phone, "person_id": person_id})
            if mail:
                ServiceMail().add({"mail": mail, "person_id": person_id})
        return ServiceUser().add({"account": account, "password": password, "person_id": person_id, "register_time": Time().to_string()})


