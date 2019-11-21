from xy.cipher.hash import Hash
from ..config import AppConfig


class RayIamHash(Hash):
    def __init__(self):
        super().__init__(**AppConfig()["hash"])

