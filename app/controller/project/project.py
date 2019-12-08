from flask import request, abort
from ...lib.flask.decorator import json_content_type
from ...lib.flask.response import response
from ...lib.flask.value_transform import ValueTransform
from ...service.project import ServiceProject
from .. import project_blueprint
from ..auth import auth


@project_blueprint.route("/", methods=["GET", "POST"])
@auth
@json_content_type()
def index():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    if request.method == "GET":
        condition = dict()
        if _id:=request.args.get("id"):
            condition.update({"id", _id})
        if name:=request.args.get("name"):
            condition.update({"name": name})
        offset = ValueTransform.intstr2int(request.args.get("offset"))
        limit = ValueTransform.intstr2int(request.args.get("limit"))
        reverse = ValueTransform.boolstr2bool(request.args.get("reverse"))
        condition_like = ValueTransform.boolstr2bool(request.args.get("condition_like"))
        if isinstance(data:=ServiceProject().get(condition, offset, limit, reverse, condition_like), list):
            rsp["code"] = 200
            rsp["data"] = data
            rsp["msg"] = "获取项目成功！"
        return response(**rsp)
    data = request.get_json()
    if not ((name:=data.get("name")) and (domain:=data.get("domain"))):
        abort(400)
    params = dict(name=name,
                  domain=domain,
                  login_url=data.get("login_url"),
                  logout_url=data.get("logout_url"),
                  auth_code=data.get("auth_code"))
    if ServiceProject().add(params):
        rsp["code"] = 200
        rsp["msg"] = "添加项目成功！"
    return response(**rsp)


@project_blueprint.route("/<int:_id>", methods=["GET", "PUT", "DELETE"])
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
            rsp["msg"] = f"获取项目：{_id} 成功！"
        elif data is None:
            rsp["code"] = 404
            rsp["msg"] = f"项目：{_id} 不存在！"
        return response(**rsp)
    condition = dict(id=_id)
    if request.method == "PUT":
        data, params = request.get_json(), dict()
        if name:=data.get("name"):
            params.update({"name": name})
        if domain:=data.get("domain"):
            params.update({"domain": domain})
        if "login_url" in data:
            params.update({"login_url": data["login_url"]})
        if "logout_url" in data:
            params.update({"logout_url": data["logout_url"]})
        if "auth_code" in data:
            params.update({"auth_code": data["auth_code"]})
        if not params:
            abort(400)
        if ServiceProject().update(condition, params):
            rsp["code"] = 200
            rsp["msg"] = f"修改项目：{_id} 成功！"
        return response(**rsp)
    if ServiceProject().delete(condition):
        rsp["code"] = 200
        rsp["msg"] = f"删除项目：{_id} 成功！"
    return response(**rsp)


