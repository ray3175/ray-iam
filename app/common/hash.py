from xy.cipher.hash import Hash
from ..config import AppConfig


class RayIamHash(Hash):
    hash_config = AppConfig().app["hash"]

    def __init__(self, hash_type=hash_config["hash_type"], salt=hash_config["salt"], iterations=hash_config["iterations"]):
        super().__init__(hash_type, salt, iterations)

