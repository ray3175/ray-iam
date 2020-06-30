from ..lib.database.session import Session
from ..dao import Dao


class Service:
    def __init__(self, dao=None):
        self.dao = dao() if callable(dao) else dao

    def new_dao(self, module=None):
        self.dao = Dao(module)

    @Session.transaction(auto_commit=False)
    def get(self, condition=None, offset=None, limit=None, reverse=False, condition_like=False, add_column=[], del_column=[]):
        return [module(add_column=add_column, del_column=del_column) for module in self.dao.get(condition, offset, limit, reverse, condition_like)]

    @Session.transaction
    def add(self, params):
        return self.dao.add(params)

    @Session.transaction
    def update(self, condition, params):
        return self.dao.update(condition, params)

    @Session.transaction
    def delete(self, condition):
        return self.dao.delete(condition)

