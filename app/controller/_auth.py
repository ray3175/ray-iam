from functools import wraps
from flask import abort, session
from ..service.auth import ServiceAuth


def auth(func):
    @wraps(func)
    def varify(*args, **kwargs):
        if not ServiceAuth().ray_sso_auth(session.get("account"), session.get("password")):
            abort(401)
        return func(*args, **kwargs)
    return varify


def max_auth(func):
    @wraps(func)
    def varify(*args, **kwargs):
        if not ServiceAuth().ray_sso_max_auth(session.get("account"), auth=99):
            abort(401)
        return func(*args, **kwargs)
    return varify


