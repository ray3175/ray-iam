import os
from xy.decorator.singleton import Singleton
from xy.models.file_models.yaml_model import YamlModel


@Singleton
class AppConfig(YamlModel):
    def __init__(self):
        self.__config_path = os.path.dirname(os.path.abspath(__file__))
        super().__init__(os.path.join(self.__config_path, "app.yaml"))
        self.data = self.data["environment-{}".format(os.getenv("ray-iam", "development"))]

    def __getitem__(self, item):
        return self.data[item]

    def get_ssl_path(self):
        ssl_path = os.path.join(self.__config_path, "ssl")
        ssl_private_key_path = os.path.join(ssl_path, self.data["ssl"]["private_key"])
        ssl_public_key_path = os.path.join(ssl_path, self.data["ssl"]["public_key"])
        return dict(private_key=ssl_private_key_path, public_key=ssl_public_key_path)

