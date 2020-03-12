from ..modules.person import Person
from . import Dao


class DaoPerson(Dao):
    def __init__(self, module=Person, session=None):
        super().__init__(module, session)

    def get_person_with_id_card(self, id_card):
        return self.session.query(self.module).filter_by(id_card=id_card).first()

    def add_person(self, id_card, name, sex, birth_date, birth_place, native_place, nationality):
        person = self.module(id_card=id_card,
                             name=name,
                             sex=sex,
                             birth_date=birth_date,
                             birth_place=birth_place,
                             native_place=native_place,
                             nationality=nationality)
        self.session.add(person)
        self.session.flush()
        return person


