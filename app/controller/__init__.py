from flask import Blueprint


default_blueprint = Blueprint("default", __name__)
project_blueprint = Blueprint("project", __name__, url_prefix="/project")
user_blueprint = Blueprint("user", __name__, url_prefix="/user")


from .default import *
from .project import *
from .user import *

