from functools import wraps
from flask import request, abort


def cross_domain(func):
    @wraps(func)
    def active(*args, **kwargs):
        rsp = func(*args, **kwargs)
        rsp.headers["Access-Control-Allow-Origin"] = "*"
        rsp.headers["Access-Control-Allow-Headers"] = "*"
        rsp.headers["Access-Control-Allow-Methods"] = "*"
        return rsp
    return active


def json_content_type(post=True, put=True, delete=True):
    methods = dict(POST=post, PUT=put, DELETE=delete)
    def action_decorator(func):
        @wraps(func)
        def action(*args, **kwargs):
            if methods.get(request.method):
                if not request.is_json:
                    abort(400)
            return func(*args, **kwargs)
        return action
    return action_decorator

