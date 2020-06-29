from flask import request, abort
from flask_cors import cross_origin
from ...lib.flask.decorator import json_content_type
from ...lib.flask.response import response
from ...service.we_chat.index import ServiceWeChat
from .. import we_chat_blueprint


@we_chat_blueprint.route("/login", methods=["GET"])
@cross_origin()
def login():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    code = request.args.get("code")
    if not code:
        abort(400)
    if data:=ServiceWeChat().get_user_with_we_chat_code(code):
        rsp["code"] = 200
        rsp["data"] = data
        rsp["msg"] = "该用户微信认证成功！"
    else:
        rsp["code"] = 202
        rsp["msg"] = "该用户尚未注册！"
    return response(**rsp)


@we_chat_blueprint.route("/register", methods=["POST"])
@cross_origin()
@json_content_type()
def register():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    data = request.get_json()
    if not ((code:=data.get("code")) and (id_card:=data.get("id_card"))):
        abort(400)
    account = data.get("account")
    password = data.get("password")
    name = data.get("name")
    sex = data.get("sex")
    birth_date = data.get("birth_date")
    birth_place = data.get("birth_place")
    native_place = data.get("native_place")
    nationality = data.get("nationality")
    phone = data.get("phone")
    mail = data.get("mail")
    if ServiceWeChat().add_user_from_we_chat_code(code, account, password, id_card, name, sex, birth_date, birth_place, native_place, nationality, phone, mail):
        rsp["code"] = 200
        rsp["msg"] = "创建用户成功！"
    return response(**rsp)


@we_chat_blueprint.route("/bind", methods=["POST"])
@cross_origin()
@json_content_type()
def bind():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    data = request.get_json()
    if not ((code:=data.get("code")) and (account:=data.get("account")) and (password:=data.get("password"))):
        abort(400)
    if ServiceWeChat().bind_user_from_we_chat_code(code, account, password):
        rsp["code"] = 200
        rsp["msg"] = "绑定用户成功！"
    return response(**rsp)


