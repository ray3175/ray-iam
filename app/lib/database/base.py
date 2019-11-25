from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

Base.dict = lambda x: recursive_func(x)


def recursive_func(x):
    _return = dict()
    for i, j in x.__dict__.items():
        if not i.startswith("_"):
            if isinstance(j, Base):
                j = recursive_func(j)
            _return.update({i: j})
    return _return

