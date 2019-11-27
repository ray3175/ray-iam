from flask import request
from ...lib.flask.decorator import json_content_type
from ...lib.flask.response import response
from ...service.project.project import ServiceProjectProject
from .. import default_blueprint
from ..auth import auth


@default_blueprint.route("/project", methods=["GET", "POST", "PUT", "DELETE"])
@auth
@json_content_type()
def project():
    if request.method == "GET":
        return response()
    data = request.get_json()
    name = data.get("name")
    domain = data.get("domain")
    logout_url = data.get("logout_url")
    license_key = data.get("license_key")
    rsp = {
        "msg": "添加项目成功！"
    }
    if not ServiceProjectProject.add_project(name, domain, logout_url, license_key):
        rsp["code"] = 400
        rsp["msg"] = "添加项目失败！"
    return response(**rsp)



