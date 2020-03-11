from flask import make_response, jsonify


def response(code=200, data=None, msg=None, **kwargs):
    return make_response(jsonify(dict(code=code, data=data, msg=msg, **kwargs)))

