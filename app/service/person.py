from ..lib.database import DB
from ..dao.person import DaoPerson
from . import Service


class ServicePerson(Service):
    def __init__(self, dao=DaoPerson):
        super().__init__(dao)

    @DB.transaction
    def get_person_obj_with_id_card(self, id_card, **kwargs):
        return self.dao.get_person_with_id_card(id_card)

    @DB.transaction
    def add_person(self, id_card, name, sex, birth_date, birth_place, native_place, nationality, **kwargs):
        return self.dao.add_person(id_card, name, sex, birth_date, birth_place, native_place, nationality)()


