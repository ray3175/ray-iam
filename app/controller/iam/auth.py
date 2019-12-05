from flask import request
from flask_cors import cross_origin
from ...lib.flask.decorator import json_content_type
from ...lib.flask.response import response
from ...service.iam.auth import ServiceIamAuth
from .. import iam_blueprint


@iam_blueprint.route("/auth", methods=["GET"])
@cross_origin()
@json_content_type()
def auth():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    account = request.args.get("account")
    password = request.args.get("password")
    if hash_password:=ServiceIamAuth().iam_auth(account, password):
        rsp["code"] = 200
        rsp["msg"] = "验证成功！"
    else:
        rsp["code"] = 400
        rsp["msg"] = "验证失败！"
    rsp["data"] = hash_password
    return response(**rsp)
