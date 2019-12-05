import os
import datetime
import flask
from xy.common.global_data import GlobalData


app = flask.Flask(__name__, static_folder="../web")


def init_app():
    from .config import AppConfig

    global_data = GlobalData()
    global_data["memory"] = dict()
    global_data["root_path"] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    global_data["log_path"] = os.path.join(global_data["root_path"], "log")
    app_config = AppConfig()

    app.config["SECRET_KEY"] = app_config["flask-config"]["SECRET_KEY"]
    app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(**app_config["flask-config"]["PERMANENT_SESSION_LIFETIME"])


def create_app():
    from .lib.flask.response import response
    from .lib.flask.redirect import redirect_to_source
    from .controller import default_blueprint, project_blueprint, user_blueprint, iam_blueprint

    app.register_blueprint(default_blueprint)
    app.register_blueprint(project_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(iam_blueprint)

    @app.errorhandler(400)
    def error_400(error):
        return response(400, msg="参数有误！")

    @app.errorhandler(401)
    def error_400(error):
        return response(401, msg="无效的权限！")

    @app.errorhandler(404)
    def error_400(error):
        return redirect_to_source("./common/error404.html")

    return app


init_app()

