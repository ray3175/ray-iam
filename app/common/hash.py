from xy.decorator.singleton import Singleton
from xy.cipher.hash import Hash
from ..config import AppConfig


@Singleton
class RayIamHash(Hash):
    def __init__(self):
        super().__init__(**AppConfig()["hash"])

