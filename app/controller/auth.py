from functools import wraps
from flask import abort, session
from ..service import Service


def auth(func):
    @wraps(func)
    def varify(*args, **kwargs):
        if not Service.ray_iam_auth(session.get("user"), session.get("password")):
            abort(401)
        return func(*args, **kwargs)
    return varify

