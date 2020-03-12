from sqlalchemy.ext.declarative import declarative_base


Module = declarative_base()

Module.__call__ = lambda x, *args, **kwargs: recursive_to_dict(x, *args, **kwargs)


def recursive_to_dict(x, *args, **kwargs):
    _return = dict()
    for i, j in x.__dict__.items():
        if not (i.startswith("_") or (kwargs.get("del_column") and i in kwargs["del_column"])):
            if isinstance(j, Module):
                j = recursive_to_dict(j, *args, **kwargs)
            _return.update({i: j})
    return _return

