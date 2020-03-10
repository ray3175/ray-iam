from flask import Blueprint


default_blueprint = Blueprint("default", __name__)
administrator_blueprint = Blueprint("administrator", __name__, url_prefix="/administrator")
project_blueprint = Blueprint("project", __name__, url_prefix="/project")
user_blueprint = Blueprint("user", __name__, url_prefix="/user")
iam_blueprint = Blueprint("iam", __name__, url_prefix="/iam")


from .default import *
from .administrator import *
from .project import *
from .user import *
from .iam import *

