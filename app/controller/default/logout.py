from flask import session
from ...lib.flask.response import response
from ...service.default.logout import ServiceDefaultLogout
from .. import default_blueprint


@default_blueprint.route("/logout", methods=["POST"])
def logout():
    rsp = {
        "code": 401,
        "msg": "当前会话不存在或已失效！"
    }
    if ServiceDefaultLogout().auth_verify(session.get("account")):
        session.pop("account", None)
        session.pop("password", None)
        rsp["code"] = 200
        rsp["msg"] = "会话注销成功！"
    return response(**rsp)



