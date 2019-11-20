from ...lib.flask.redirect import redirect_to_endpoint, redirect_to_source
from .. import default_blueprint


@default_blueprint.route("/", methods=["GET"])
def _index():
    return redirect_to_endpoint("default.index")


@default_blueprint.route("/index", methods=["GET"])
def index():
    if not 0:
        return redirect_to_source("./platform/login/index.html")
    return redirect_to_source("./platform/index.html")

