from xy.cipher.hash import Hash
from xy.common.global_data import GlobalData
from ..config import AppConfig


class RayIamHash(Hash):
    def __init__(self):
        super().__init__(**AppConfig()[GlobalData().get("environment", "environment-development")]["hash"])

