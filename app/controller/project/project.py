from flask import request
from ...lib.flask.decorator import json_content_type
from ...lib.flask.response import response
from ...lib.flask.value_transform import ValueTransform
from ...service.project.project import ServiceProjectProject
from .. import project_blueprint
from ..auth import auth


@project_blueprint.route("/", methods=["GET", "POST"])
@auth
@json_content_type()
def project():
    if request.method == "GET":
        _id = request.args.get("id")
        name = request.args.get("name")
        condition = dict()
        if _id:
            condition.update({"id", _id})
        if name:
            condition.update({"name": name})
        offset = ValueTransform.intstr2int(request.args.get("offset"))
        limit = ValueTransform.intstr2int(request.args.get("limit"))
        reverse = ValueTransform.boolstr2bool(request.args.get("reverse"))
        rsp = {
            "code": 500,
            "msg": "服务器出现未知错误，请联系管理员！"
        }
        if isinstance(data:=ServiceProjectProject().get(condition, offset, limit, reverse), list):
            rsp["code"] = 200
            rsp["data"] = data
            rsp["msg"] = "获取项目成功！"
        return response(**rsp)
    data = request.get_json()
    params = dict(name=data.get("name"),
                  domain=data.get("domain"),
                  login_url=data.get("login_url"),
                  logout_url=data.get("logout_url"),
                  auth_code=data.get("auth_code"))
    rsp = {
        "msg": "添加项目成功！"
    }
    if not ServiceProjectProject().add(params):
        rsp["code"] = 400
        rsp["msg"] = "添加项目失败！"
    return response(**rsp)


