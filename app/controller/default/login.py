from flask import request, session, abort
from ...lib.flask.decorator import json_content_type
from ...lib.flask.response import response
from ...lib.flask.redirect import redirect_to_source
from ...service.default.login import ServiceDefaultLogin
from .. import default_blueprint


@default_blueprint.route("/login", methods=["GET", "POST"])
@json_content_type()
def login():
    if request.method == "GET":
        return redirect_to_source("./platform/login/index.html")
    data = request.get_json()
    if not ((user:=data.get("user")) and (password:=data.get("password"))):
        abort(401)
    rsp = {
        "code": 401,
        "msg": "账号不存在或密码不正确！"
    }
    if ServiceDefaultLogin().auth_verify(user, password):
        session["user"] = user
        session["password"] = password
        rsp["code"] = 200
        rsp["msg"] = "验证通过！"
    return response(**rsp)



