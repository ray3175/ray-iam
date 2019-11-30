from ..lib.database import DB


class Service:
    def __init__(self, dao):
        self.dao = dao()

    @DB.transaction(auto_commit=False)
    def get(self, condition=None, offset=None, limit=None, reverse=False, **kwargs):
        return [module.dict() for module in self.dao.get(condition, offset, limit, reverse, **kwargs)]

    @DB.transaction
    def add(self, params, **kwargs):
        return self.dao.add(params, **kwargs)

    @DB.transaction
    def update(self, condition, params, **kwargs):
        return self.dao.update(condition, params, **kwargs)

    @DB.transaction
    def delete(self, condition, params, **kwargs):
        return self.dao.delete(condition, params, **kwargs)

