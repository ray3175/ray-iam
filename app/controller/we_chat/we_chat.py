from flask import request, abort
from flask_cors import cross_origin
from xy.exception import XYException
from ...lib.flask.decorator import json_content_type
from ...lib.flask.response import response
from ...service.we_chat.we_chat import ServiceWeChart
from .. import iam_blueprint


@iam_blueprint.route("/we_chat", methods=["GET"])
@cross_origin()
@json_content_type()
def we_chat():
    """
    通过Code，获取用户的信息。
    :return:
    """
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    code = request.args.get("code")
    if not code:
        abort(400)
    try:
        ServiceWeChart().code2Session(code)
    except XYException as e:
        rsp["msg"] = e.msg
    return response(**rsp)



