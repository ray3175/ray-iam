from abc import ABC, abstractmethod
from xy.common.global_data import GlobalData


class Memory(ABC):
    memory = GlobalData()["memory"]

    @abstractmethod
    def cache_memory(self, name, args_name):
        pass

