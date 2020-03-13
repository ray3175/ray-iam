from flask import request, abort
from flask_cors import cross_origin
from ...config import AppConfig
from ...lib.flask.decorator import json_content_type
from ...lib.flask.response import response
from ...service.iam.we_chat import ServiceIamWeChat
from .. import iam_blueprint
from ._auth import auth


cookie_config = AppConfig()["token-config"]


@iam_blueprint.route("/we_chat", methods=["GET", "POST"])
@cross_origin()
@auth
@json_content_type()
def we_chat():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    if not (token:=request.args.get(cookie_config["key"]) if request.method == "GET" else request.get_json().get(cookie_config["key"])):
        abort(400)
    if data:=ServiceIamWeChat().get_we_chat_user_with_token(token):
        rsp["code"] = 200
        rsp["data"] = data
        rsp["msg"] = "该用户微信已登录成功！"
    else:
        rsp["code"] = 202
        rsp["msg"] = "该用户微信尚未登录！"
    return response(**rsp)


@iam_blueprint.route("/we_chat/logout", methods=["GET", "POST"])
@cross_origin()
@auth
@json_content_type()
def we_chat_logout():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    if not (token:=request.args.get(cookie_config["key"]) if request.method == "GET" else request.get_json().get(cookie_config["key"])):
        abort(400)
    if data:=ServiceIamWeChat().logout_we_chat_user_with_token(token):
        rsp["code"] = 200
        rsp["data"] = data
        rsp["msg"] = "该用户微信已登出成功！"
    else:
        rsp["code"] = 202
        rsp["msg"] = "该用户微信尚未登录！"
    return response(**rsp)

