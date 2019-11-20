from functools import wraps


def active_cross_domain(func):
    @wraps(func)
    def cross_domain(*args, **kwargs):
        rsp = func(*args, **kwargs)
        rsp.headers["Access-Control-Allow-Origin"] = "*"
        rsp.headers["Access-Control-Allow-Headers"] = "*"
        rsp.headers["Access-Control-Allow-Methods"] = "*"
        return rsp
    return cross_domain

