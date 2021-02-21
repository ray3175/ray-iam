from flask import Blueprint


default_blueprint = Blueprint("default", __name__)
administrator_blueprint = Blueprint("administrator", __name__, url_prefix="/administrator")
project_blueprint = Blueprint("project", __name__, url_prefix="/project")
user_blueprint = Blueprint("user", __name__, url_prefix="/user")
sso_blueprint = Blueprint("sso", __name__, url_prefix="/sso")
we_chat_blueprint = Blueprint("we_chat", __name__, url_prefix="/we_chat")


from .default import *
from .administrator import *
from .project import *
from .user import *
from .sso import *
from .we_chat import *

