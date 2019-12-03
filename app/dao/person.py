from ..modules.person import Person
from . import Dao


class DaoPerson(Dao):
    def __init__(self, module=Person, session=None):
        super().__init__(module, session)

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


