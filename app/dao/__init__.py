from ..lib.database import DB


class Dao:
    def __init__(self, module=None, session=None):
        self.module = module
        self.session = session if session else DB.Session()

    def _get_condition(self, condition):
        _condition = list()
        for key, value in condition.items():
            _condition.append(getattr(self.module, key) == value)
        return _condition

    def get(self, condition=None, offset=None, limit=None, reverse=False):
        module = self.session.query(self.module)
        if condition and isinstance(condition, dict):
            module = module.filter(*self._get_condition(condition))
        if reverse:
            module = module.order_by(self.module.id.desc())
        if limit:
            module = module.limit(limit)
        if offset:
            module = module.offset(offset)
        return module.all()

    def add(self, params):
        self.session.add(self.module(**params))
        return True

    def update(self, condition, params):
        self.session.query(self.module).filter(*self._get_condition(condition)).update(params, synchronize_session=False)
        return True

    def delete(self, condition):
        self.session.query(self.module).filter(*self._get_condition(condition)).delete(synchronize_session=False)
        return True
