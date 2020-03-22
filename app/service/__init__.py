from ..lib.database import DB
from ..dao import Dao


class Service:
    def __init__(self, dao=Dao):
        self.dao = dao()

    @DB.transaction(auto_commit=False)
    def get(self, condition=None, offset=None, limit=None, reverse=False, condition_like=False, add_column=[], del_column=[], **kwargs):
        return [module(add_column=add_column.copy(), del_column=del_column) for module in self.dao.get(condition, offset, limit, reverse, condition_like)]

    @DB.transaction
    def add(self, params, **kwargs):
        return self.dao.add(params)

    @DB.transaction
    def update(self, condition, params, **kwargs):
        return self.dao.update(condition, params)

    @DB.transaction
    def delete(self, condition, **kwargs):
        return self.dao.delete(condition)

