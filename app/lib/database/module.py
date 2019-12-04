from sqlalchemy.ext.declarative import declarative_base


Module = declarative_base()

Module.__call__ = lambda x: recursive_to_dict(x)


def recursive_to_dict(x):
    _return = dict()
    for i, j in x.__dict__.items():
        if not i.startswith("_"):
            if isinstance(j, Module):
                j = recursive_to_dict(j)
            _return.update({i: j})
    return _return

