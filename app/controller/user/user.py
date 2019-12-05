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
            if data:=ServiceUser().get_user_with_account_with_cache_priority(account):
                rsp["code"] = 200
                rsp["data"] = [data]
                rsp["msg"] = f"获取用户账号：{account} 成功！"
            elif data is None:
                rsp["code"] = 400
                rsp["data"] = []
                rsp["msg"] = f"用户账号：{account} 不存在！"
        else:
            offset = ValueTransform.intstr2int(request.args.get("offset"))
            limit = ValueTransform.intstr2int(request.args.get("limit"))
            reverse = ValueTransform.boolstr2bool(request.args.get("reverse"))
            if isinstance(data:=ServiceUser().get(offset=offset, limit=limit, reverse=reverse), list):
                rsp["code"] = 200
                rsp["data"] = data
                rsp["msg"] = "获取用户成功！"
        return response(**rsp)
    data = request.get_json()
    if not ((account:=data.get("account")) and (password:=data.get("password"))):
        abort(400)
    params = dict(account=account,
                  password=password,
                  person_id=data.get("person_id"))
    if x:=ServiceUser().add(params):
        rsp["code"] = 200
        rsp["msg"] = "添加用户成功！"
    return response(**rsp)


@user_blueprint.route("/<int:_id>", methods=["GET", "PUT", "DELETE"])
@auth
@json_content_type(delete=False)
def user(_id):
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    if request.method == "GET":
        if data:=ServiceUser().get_user(_id):
            rsp["code"] = 200
            rsp["data"] = data
            rsp["msg"] = f"获取用户：{_id} 成功！"
        elif data is None:
            rsp["code"] = 404
            rsp["msg"] = f"用户：{_id} 不存在！"
        return response(**rsp)
    condition = dict(id=_id)
    if request.method == "PUT":
        data, params = request.get_json(), dict()
        if account:=data.get("account"):
            params.update({"account": account})
        if password:=data.get("password"):
            params.update({"password": password})
        if person_id:=data.get("person_id"):
            params.update({"person_id": person_id})
        if not params:
            abort(400)
        if ServiceUser().update(condition, params):
            rsp["code"] = 200
            rsp["msg"] = f"修改用户：{_id} 成功！"
        return response(**rsp)
    if ServiceUser().delete(condition):
        rsp["code"] = 200
        rsp["msg"] = f"删除用户：{_id} 成功！"
    return response(**rsp)


@user_blueprint.route("/logic/<any(delete, restore):action>/<int:_id>", methods=["PUT"])
@auth
@json_content_type(put=False)
def user_logic_action(action, _id):
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    if ServiceUser().update({"id": _id}, {"xy": False if action == "delete" else True}):
        rsp["code"] = 200
        rsp["msg"] = f'{"删除" if action == "delete" else "恢复"}（逻辑）用户：{_id} 成功！'
    return response(**rsp)

