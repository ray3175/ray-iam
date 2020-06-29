from xy.utils.time import Time
from ..lib.database.session import Session
from ..dao.person import DaoPerson
from . import Service


class ServicePerson(Service):
    def __init__(self, dao=DaoPerson):
        super().__init__(dao)

    @Session.transaction(auto_commit=False)
    def get_person_obj_with_id_card(self, id_card):
        return self.dao.get_person_with_id_card(id_card)

    @Session.transaction
    def add_person(self, id_card, name, sex, birth_date, birth_place, native_place, nationality):
        return self.dao.add_person(id_card, name, sex, birth_date, birth_place, native_place, nationality, Time().to_string())()


