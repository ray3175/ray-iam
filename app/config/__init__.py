import os
import asyncio
from concurrent.futures import ThreadPoolExecutor
from xy.stdlib_overwrite.dict import Dict
from xy.decorator.singleton import Singleton
from xy.common.models.file_system.directory import DirectoryModel
from xy.common.models.file_system.file.yaml import YamlModel


@Singleton
class AppConfig:
    def __init__(self):
        self.__config_path = os.path.dirname(os.path.abspath(__file__))
        dir_model = DirectoryModel(self.__config_path)
        dir_model.scan_directory(scan_iterate=True, file_regex=".*\.yaml", file_model=YamlModel)
        self.__data = asyncio.run(self.__init_yaml_data(dir_model.documents, ThreadPoolExecutor(max_workers=os.cpu_count(), thread_name_prefix="ray-sso.app.AppConfig")))
        self.__environment = f"environment-{os.getenv('ray-sso', 'development')}"

    async def __load_yaml_data(self, yaml, executor):
        return await asyncio.get_event_loop().run_in_executor(executor, yaml.read_data, "utf-8")

    async def __init_yaml_data(self, document, executor):
        data = Dict()
        for yaml in document:
            if isinstance(yaml, DirectoryModel):
                data[yaml.name] = asyncio.create_task(self.__init_yaml_data(yaml.documents, executor))
            elif isinstance(yaml, YamlModel):
                data[yaml.name.removesuffix(".yaml")] = asyncio.create_task(self.__load_yaml_data(yaml, executor))
        for key, value in data.items():
            data[key] = await value
        return data

    def __getitem__(self, item):
        return self.__data[item][self.__environment]

    def __getattr__(self, item):
        return self[item]

