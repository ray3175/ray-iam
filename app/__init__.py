import os
import datetime
import flask
from .common.global_data import GlobalData


app = flask.Flask(__name__, static_folder="../web")


def init_app():
    from .config import AppConfig

    global_data = GlobalData()
    global_data["root_path"] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    global_data["log_path"] = os.path.join(global_data["root_path"], "log")
    app_config = AppConfig()

    app.config["SECRET_KEY"] = app_config.flask["flask-config"]["SECRET_KEY"]
    app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(**app_config.flask["flask-config"]["PERMANENT_SESSION_LIFETIME"])


def create_app():
    from .lib.flask.errorhandler import Errorhandler
    from .controller import default_blueprint, administrator_blueprint, project_blueprint, user_blueprint, sso_blueprint, we_chat_blueprint

    app.register_blueprint(default_blueprint)
    app.register_blueprint(administrator_blueprint)
    app.register_blueprint(project_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(sso_blueprint)
    app.register_blueprint(we_chat_blueprint)

    return app


init_app()

