import os
from xy.decorator.singleton import Singleton
from xy.models.file_models.yaml_model import YamlModel


@Singleton
class AppConfig(YamlModel):
    def __init__(self):
        super().__init__(os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.yaml"))

    def __getitem__(self, item):
        return self.data[item]

