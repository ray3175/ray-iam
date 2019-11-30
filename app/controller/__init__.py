from flask import Blueprint


default_blueprint = Blueprint("default", __name__)
project_blueprint = Blueprint("project", __name__, url_prefix="/project")


from .default import *
from .project import *

