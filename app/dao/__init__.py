from ..lib.database import DB


class Dao:
    def __init__(self, module=None):
        self.module = module
        self.session = None

    def _get_condition(self, condition):
        _condition = list()
        for key, value in condition.items():
            _condition.append(getattr(self.module, key) == value)
        return _condition

    @DB.session
    def get(self, condition=None, offset=None, limit=None, reverse=False, **kwargs):
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

    @DB.session
    def add(self, params, **kwargs):
        self.session.add(self.module(**params))
        return True

    @DB.session
    def update(self, condition, params, **kwargs):
        self.session.query(self.module).filter(*self._get_condition(condition)).update(params, synchronize_session=False)
        return True

    @DB.session
    def delete(self, condition, **kwargs):
        self.session.query(self.module).filter(*self._get_condition(condition)).delete(synchronize_session=False)
        return True

