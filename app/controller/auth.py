from functools import wraps
from flask import abort, session
from ..service.auth import ServiceAuth


def auth(func):
    @wraps(func)
    def varify(*args, **kwargs):
        if not ServiceAuth().ray_iam_auth(session.get("user"), session.get("password")):
            abort(401)
        return func(*args, **kwargs)
    return varify

