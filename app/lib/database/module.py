from sqlalchemy.ext.declarative import declarative_base


Module = declarative_base()

Module.__call__ = lambda x, *args, **kwargs: recursive_to_dict(x, *args, **kwargs)


def recursive_to_dict(x, *args, **kwargs):
    _return = dict()
    for i, j in x.__dict__.items():
        if not (i.startswith(("_", "*")) or (kwargs.get("del_column") and i in kwargs["del_column"])):
            _return.update({i: j})
    add_column_copy = kwargs.get("add_column", []).copy()
    for i in kwargs.get("add_column", []):
        if y:=getattr(x, i, None) or getattr(x, f"*{i}_from_{x.__tablename__}*", None):
            add_column_copy.remove(i)
            if isinstance(y, Module):
                y = y(add_column=add_column_copy, del_column=kwargs.get("del_column"))
            elif isinstance(y, list):
                y = [y(add_column=add_column_copy, del_column=kwargs.get("del_column")) for y in y]
            _return.update({i: y})
    return _return

