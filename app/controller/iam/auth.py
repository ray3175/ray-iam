from flask import request, abort
from ...lib.flask.decorator import cross_domain, json_content_type
from ...lib.flask.response import response
from ...service.project import ServiceProject
from ...service.iam.auth import ServiceIamAuth
from .. import iam_blueprint


@iam_blueprint.route("/auth", methods=["GET"])
@cross_domain
def auth():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    if not ((account:=request.args.get("account")) and (password:=request.args.get("password"))):
        abort(400)
    if hash_account:=ServiceIamAuth().iam_auth(account, password):
        rsp["code"] = 200
        rsp["msg"] = "认证成功！"
    else:
        rsp["code"] = 400
        rsp["msg"] = "认证失败！"
    rsp["data"] = hash_account
    return response(**rsp)


@iam_blueprint.route("/auth/hash_account", methods=["GET"])
@cross_domain
def auth_hash_account():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    if not (hash_account:=request.args.get("hash_account")):
        abort(400)
    if user:=ServiceIamAuth().get_user_with_hash_account(hash_account):
        rsp["code"] = 200
        rsp["msg"] = "获取用户成功！"
    else:
        rsp["code"] = 400
        rsp["msg"] = "获取用户失败！"
    rsp["data"] = user
    return response(**rsp)


@iam_blueprint.route("/login", methods=["POST"])
@cross_domain
@json_content_type()
def login():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    data = request.get_json()
    if not ((hash_account:=data.get("hash_account")) and isinstance(project:=data.get("project"), dict) and (project_name:=project.get("name")) and (project_auth_code:=project.get("auth_code"))):
        abort(400)
    if ServiceProject().get({"name": project_name, "auth_code": project_auth_code}):
        if (service_iam_auth:=ServiceIamAuth()) and (user:=service_iam_auth.get_user_with_hash_account(hash_account)):
            if service_iam_auth.active_hash_account_to_all_project(hash_account, user):
                rsp["code"] = 200
                rsp["msg"] = "激活所有项目成功！"
        else:
            rsp["code"] = 202
            rsp["msg"] = "哈希账号不存在或已失效！"
    else:
        rsp["code"] = 401
        rsp["msg"] = "项目名称与授权码不匹配！"
    return response(**rsp)


@iam_blueprint.route("/logout", methods=["POST"])
@cross_domain
@json_content_type()
def logout():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    data = request.get_json()
    if not ((hash_account:=data.get("hash_account")) and isinstance(project:=data.get("project"), dict) and (project_name:=project.get("name")) and (project_auth_code:=project.get("auth_code"))):
        abort(400)
    if ServiceProject().get({"name": project_name, "auth_code": project_auth_code}):
        if ServiceIamAuth().logout_hash_account_to_all_project(hash_account):
            rsp["code"] = 200
            rsp["msg"] = "注销所有项目成功！"
    else:
        rsp["code"] = 401
        rsp["msg"] = "项目名称与授权码不匹配！"
    return response(**rsp)

