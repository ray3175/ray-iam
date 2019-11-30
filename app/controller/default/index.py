from flask import session
from ...lib.flask.redirect import redirect_to_endpoint, redirect_to_source
from ...service.auth import ServiceAuth
from .. import default_blueprint


@default_blueprint.route("/", methods=["GET"])
def _index():
    return redirect_to_endpoint("default.index")


@default_blueprint.route("/index", methods=["GET"])
def index():
    if ServiceAuth().ray_iam_auth(session.get("user"), session.get("password")):
        return redirect_to_source("./platform/index.html")
    return redirect_to_source("./platform/login/index.html")

