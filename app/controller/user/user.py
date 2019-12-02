from flask import request, abort
from ...lib.flask.decorator import json_content_type
from ...lib.flask.response import response
from ...lib.flask.value_transform import ValueTransform
from ...service.user import ServiceUser
from .. import user_blueprint
from ..auth import auth


@user_blueprint.route("/", methods=["GET", "POST"])
@auth
@json_content_type()
def index():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    if request.method == "GET":
        if account:=request.args.get("account"):
            if data:=ServiceUser().get_user_with_account(account):
                rsp["code"] = 200
                rsp["data"] = [data]
                rsp["msg"] = f"获取用户账号：{account} 成功！"
            elif data is None:
                rsp["code"] = 400
                rsp["msg"] = f"用户账号：{account} 不存在！"
        else:
            offset = ValueTransform.intstr2int(request.args.get("offset"))
            limit = ValueTransform.intstr2int(request.args.get("limit"))
            reverse = ValueTransform.boolstr2bool(request.args.get("reverse"))
            if isinstance(data:=ServiceUser().get({"xy": True}, offset, limit, reverse), list):
                rsp["code"] = 200
                rsp["data"] = data
                rsp["msg"] = "获取用户成功！"
        return response(**rsp)
    data = request.get_json()
    if not ((account:=data.get("account")) and (password:=data.get("password"))):
        abort(400)
    id_card = data.get("id_card")
    name = data.get("name")
    sex = data.get("sex")
    birth_date = data.get("birth_date")
    birth_place = data.get("birth_place")
    native_place = data.get("native_place")
    nationality = data.get("nationality")
    phone = data.get("phone")
    mail = data.get("mail")
    if ServiceUser().add_user(account, password, id_card, name, sex, birth_date, birth_place, native_place, nationality, phone, mail):
        rsp["code"] = 200
        rsp["msg"] = "添加用户成功！"
    return response(**rsp)


@user_blueprint.route("/<int:_id>", methods=["GET", "PUT", "DELETE"])
@auth
@json_content_type(delete=False)
def project(_id):
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    if request.method == "GET":
        if data:=ServiceProject().get_project(_id):
            rsp["code"] = 200
            rsp["data"] = data
            rsp["msg"] = f"获取用户：{_id} 成功！"
        elif data is None:
            rsp["code"] = 404
            rsp["msg"] = f"用户：{_id} 不存在！"
        return response(**rsp)
    else:
        condition = dict(id=_id)
        if request.method == "PUT":
            data, params = request.get_json(), dict()
            if name:=data.get("name"):
                params.update({"name": name})
            if domain:=data.get("domain"):
                params.update({"domain": domain})
            if login_url:=data.get("login_url"):
                params.update({"login_url": login_url})
            if logout_url:=data.get("logout_url"):
                params.update({"logout_url": logout_url})
            if auth_code:=data.get("auth_code"):
                params.update({"auth_code": auth_code})
            if not params:
                abort(400)
            if ServiceProject().update(condition, params):
                rsp["code"] = 200
                rsp["msg"] = f"修改用户：{_id} 成功！"
            return response(**rsp)
        if ServiceProject().delete(condition):
            rsp["code"] = 200
            rsp["msg"] = f"删除用户：{_id} 成功！"
        return response(**rsp)


