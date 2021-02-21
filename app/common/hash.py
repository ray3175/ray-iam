from xy.cipher.hash import Hash
from xy.cipher.code import Code
from ..config import AppConfig


class RaySSOHash(Hash, Code):
    hash_config = AppConfig().app["hash"]

    def __init__(self, hash_type=hash_config["hash_type"], salt=hash_config["salt"], iterations=hash_config["iterations"]):
        super(RaySSOHash, self).__init__(hash_type, salt, iterations)
        super(Hash, self).__init__("hex")

    def encrypt(self, text):
        hash_bytes = super().encrypt(text.encode("utf-8"))
        return super().encode(hash_bytes).decode("utf-8")

