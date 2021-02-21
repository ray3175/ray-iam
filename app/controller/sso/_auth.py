from functools import wraps
from flask import request, abort
from ...service.auth import ServiceAuth


def auth(func):
    @wraps(func)
    def varify(*args, **kwargs):
        project_name, project_auth_code = request.headers.get("project_name") or request.args.get("project_name"), request.headers.get("project_auth_code") or request.args.get("project_auth_code")
        if not ServiceAuth().project_sso_auth(project_name, project_auth_code):
            abort(401)
        return func(*args, **kwargs)
    return varify

