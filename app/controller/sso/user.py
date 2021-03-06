from flask import request, abort
from flask_cors import cross_origin
from ...lib.flask.decorator import json_content_type
from ...lib.flask.response import response
from ...lib.flask.value_transform import ValueTransform
from ...service.user import ServiceUser
from ...service.sso.user import ServiceSSOUser
from .. import sso_blueprint
from ._auth import auth


@sso_blueprint.route("/user", methods=["GET", "POST", "PUT", "DELETE"])
@cross_origin()
@auth
@json_content_type()
def user():
    rsp = {
        "code": 500,
        "msg": "服务器出现未知错误，请联系管理员！"
    }
    if request.method == "GET":
        condition = dict(xy=True)
        if account:=request.args.get("account"):
            condition.update({"account": account})
        offset = ValueTransform.intstr2int(request.args.get("offset"))
        limit = ValueTransform.intstr2int(request.args.get("limit"))
        reverse = ValueTransform.boolstr2bool(request.args.get("reverse"))
        condition_like = ValueTransform.boolstr2bool(request.args.get("condition_like"))
        if isinstance(data:=ServiceUser().get(condition, offset, limit, reverse, condition_like, add_column=["person", "phone", "mail", "we_chat_user"], del_column=["password"]), list):
            rsp["code"] = 200
            rsp["data"] = data
            rsp["msg"] = "获取用户成功！"
        return response(**rsp)
    data = request.get_json()
    if request.method == "POST":
        if not ((account:=data.get("account")) and (password:=data.get("password"))):
            abort(400)
        id_card = data.get("id_card")
        name = data.get("name")
        sex = data.get("sex")
        birth_date = data.get("birth_date")
        birth_place = data.get("birth_place")
        native_place = data.get("native_place")
        nationality = data.get("nationality")
        phone = data.get("phone")
        mail = data.get("mail")
        if ServiceSSOUser().add_user(account, password, id_card, name, sex, birth_date, birth_place, native_place, nationality, phone, mail):
            rsp["code"] = 200
            rsp["msg"] = "添加用户成功！"
    else:
        if not (_id:=data.get("id")):
            abort(400)
        condition = dict(id=_id)
        params = dict() if request.method == "PUT" else dict(xy=False)
        if "account" in data:
            params.update({"account": data["account"]})
        if "password" in data:
            params.update({"password": data["password"]})
        if not params:
            abort(400)
        if ServiceUser().update(condition, params):
            rsp["code"] = 200
            rsp["msg"] = f"{'修改' if request.method=='PUT' else '删除'}用户：{_id} 成功！"
    return response(**rsp)
