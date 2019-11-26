from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

Base.dict = lambda x: recursive_to_dict(x)


def recursive_to_dict(x):
    _return = dict()
    for i, j in x.__dict__.items():
        if not i.startswith("_"):
            if isinstance(j, Base):
                j = recursive_to_dict(j)
            _return.update({i: j})
    return _return

