import os
from .. import AppConfig


class AppConfigSSL:
    config_ssl_path = os.path.dirname(os.path.abspath(__file__))
    private_key = AppConfig().flask["ssl"]["private_key"]
    public_key = AppConfig().flask["ssl"]["public_key"]

    @classmethod
    def get_ssl_path(cls):
        ssl_private_key_path = os.path.join(cls.config_ssl_path, cls.private_key)
        ssl_public_key_path = os.path.join(cls.config_ssl_path, cls.public_key)
        return dict(private_key=ssl_private_key_path, public_key=ssl_public_key_path)

