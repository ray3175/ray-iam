import os
from xy.decorator.singleton import Singleton
from xy.models.dir_models.yaml import YamlDirModel


@Singleton
class AppConfig(YamlDirModel):
    def __init__(self):
        self.__config_path = os.path.dirname(os.path.abspath(__file__))
        super().__init__(self.__config_path)
        self.__data = super().get_data()
        self.__environment = f"environment-{os.getenv('ray-iam', 'development')}"

    def __getitem__(self, item):
        return self.__data[item].get_data()[self.__environment]

    def __getattr__(self, item):
        return self[item]

