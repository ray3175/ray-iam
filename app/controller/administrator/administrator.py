from flask import request, session, abort
from ...lib.flask.decorator import json_content_type
from ...lib.flask.response import response
from ...lib.flask.value_transform import ValueTransform
from ...service.administrator import ServiceAdministrator
from .. import administrator_blueprint
from .._auth import auth, max_auth


@administrator_blueprint.route("/", methods=["GET", "POST"])
@auth
@max_auth
@json_content_type()
def index():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    if request.method == "GET":
        condition = dict()
        if account:=request.args.get("account"):
            condition.update({"account": account})
        offset = ValueTransform.intstr2int(request.args.get("offset"))
        limit = ValueTransform.intstr2int(request.args.get("limit"))
        reverse = ValueTransform.boolstr2bool(request.args.get("reverse"))
        condition_like = ValueTransform.boolstr2bool(request.args.get("condition_like"))
        if isinstance(data:=ServiceAdministrator().get(condition, offset, limit, reverse, condition_like), list):
            rsp["code"] = 200
            rsp["data"] = data
            rsp["msg"] = "获取管理员成功！"
        return response(**rsp)
    data = request.get_json()
    if not ((account:=data.get("account")) and (password:=data.get("password"))):
        abort(400)
    params = dict(account=account,
                  password=password,
                  auth=data.get("auth"),
                  remark=data.get("remark"))
    if ServiceAdministrator().add(params):
        rsp["code"] = 200
        rsp["msg"] = "添加管理员成功！"
    return response(**rsp)


@administrator_blueprint.route("/<int:_id>", methods=["GET", "PUT", "DELETE"])
@auth
@max_auth
@json_content_type(delete=False)
def administrator(_id):
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    if request.method == "GET":
        if data:=ServiceAdministrator().get_administrator(_id):
            rsp["code"] = 200
            rsp["data"] = data
            rsp["msg"] = f"获取管理员：{_id} 成功！"
        elif data is None:
            rsp["code"] = 404
            rsp["msg"] = f"管理员：{_id} 不存在！"
        return response(**rsp)
    condition = dict(id=_id)
    if request.method == "PUT":
        data, params = request.get_json(), dict()
        if password:=data.get("password"):
            params.update({"password": password})
        if auth:=data.get("auth"):
            params.update({"auth": auth})
        if remark:=data.get("remark"):
            params.update({"remark": remark})
        if not params:
            abort(400)
        if ServiceAdministrator().update(condition, params):
            rsp["code"] = 200
            rsp["msg"] = f"修改管理员：{_id} 成功！"
        return response(**rsp)
    if ServiceAdministrator().delete(condition):
        rsp["code"] = 200
        rsp["msg"] = f"删除管理员：{_id} 成功！"
    return response(**rsp)


@administrator_blueprint.route("/update_password_with_self", methods=["GET", "PUT"])
@auth
@json_content_type()
def update_self_password():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    account = session.get("account")
    if request.method == "GET":
        if data:=ServiceAdministrator().get_administrator_with_user_priority_cache_memory(account):
            rsp["code"] = 200
            rsp["data"] = data
            rsp["msg"] = "个人信息获取成功！"
        return response(**rsp)
    data = request.get_json()
    password = data.get("password")
    if ServiceAdministrator().update({"account": account}, {"password": password}):
        rsp["code"] = 200
        rsp["msg"] = "密码更新成功！"
    return response(**rsp)

