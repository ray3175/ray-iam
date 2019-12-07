from flask import request, abort, redirect, make_response
from flask_cors import cross_origin
from ...config import AppConfig
from ...lib.flask.decorator import json_content_type
from ...lib.flask.response import response
from ...service.project import ServiceProject
from ...service.iam.auth import ServiceIamAuth
from .. import iam_blueprint


@iam_blueprint.route("/", methods=["GET"])
@cross_origin()
def index():
    cookie_config = AppConfig()["cookie-config"]
    if not (_redirect:=request.args.get("redirect", "") or request.headers.get("Referer", "")):
        abort(401)
    params = f"{'&' if '?' in _redirect else '?'}{cookie_config['key']}={hash_account}" if (hash_account:=request.cookies.get(cookie_config["key"])) and ServiceIamAuth().get_user_with_hash_account(hash_account) else ""
    return redirect(_redirect + params)


@iam_blueprint.route("/auth", methods=["GET", "POST"])
@cross_origin()
@json_content_type()
def auth():
    cookie_config = AppConfig()["cookie-config"]
    if request.method == "GET":
        if not (_redirect:=request.args.get("redirect", "") or request.headers.get("Referer", "")):
            abort(401)
        params = f"{'&' if '?' in _redirect else '?'}{cookie_config['key']}={hash_account}" if (account:=request.args.get("account")) and (password:=request.args.get("password")) and (hash_account:=ServiceIamAuth().iam_auth(account, password)) else ""
        rsp = make_response(redirect(_redirect + params))
        if hash_account:
            rsp.set_cookie(value=hash_account, **cookie_config)
        return rsp
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    data = request.get_json()
    if not (hash_account:=data.get(cookie_config["key"])):
        abort(400)
    if user:=ServiceIamAuth().get_user_with_hash_account(hash_account):
        rsp["code"] = 200
        rsp["msg"] = "获取用户成功！"
    else:
        rsp["code"] = 400
        rsp["msg"] = "获取用户失败！"
    rsp["data"] = user
    return response(**rsp)


@iam_blueprint.route("/auth/account", methods=["GET"])
@cross_origin()
def auth_account():
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


@iam_blueprint.route("/login", methods=["POST"])
@cross_origin()
@json_content_type()
def login():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    data = request.get_json()
    if not ((hash_account:=data.get("hash_account") and data.get("xy-auth")) and isinstance(project:=data.get("project"), dict) and (project_name:=project.get("name")) and (project_auth_code:=project.get("auth_code"))):
        abort(400)
    if ServiceProject().get({"name": project_name, "auth_code": project_auth_code}):
        if (service_iam_auth:=ServiceIamAuth()) and (user:=service_iam_auth.get_user_with_hash_account(hash_account)):
            if service_iam_auth.active_hash_account_to_all_project(hash_account, user):
                rsp["code"] = 202
                rsp["msg"] = "已激活所有项目！"
        else:
            rsp["code"] = 204
            rsp["msg"] = "哈希账号不存在或已失效！"
    else:
        rsp["code"] = 401
        rsp["msg"] = "项目名称与授权码不匹配！"
    return response(**rsp)


@iam_blueprint.route("/logout", methods=["POST"])
@cross_origin()
@json_content_type()
def logout():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    data = request.get_json()
    if not ((hash_account:=data.get("hash_account") and data.get("xy-auth")) and isinstance(project:=data.get("project"), dict) and (project_name:=project.get("name")) and (project_auth_code:=project.get("auth_code"))):
        abort(400)
    if ServiceProject().get({"name": project_name, "auth_code": project_auth_code}):
        if ServiceIamAuth().logout_hash_account_to_all_project(hash_account):
            rsp["code"] = 202
            rsp["msg"] = "已注销所有项目！"
    else:
        rsp["code"] = 401
        rsp["msg"] = "项目名称与授权码不匹配！"
    return response(**rsp)

