from functools import wraps
from xy.decorator.singleton import Singleton
from xy.common.global_data import GlobalData
from . import Cache


@Singleton
class CacheMemory(Cache):
    def __init__(self):
        self.__memory = GlobalData()["memory"] = dict()

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, _memory):
        self.__memory = _memory

    @memory.deleter
    def memory(self):
        self.__memory.clear()

    def cache(self, name, args_name, *args, **kwargs):
        def cache_action(func):
            @wraps(func)
            def action(*args, **kwargs):
                if args_value:=self._extract_args_value(func, args_name, *args, **kwargs) if args_name else None:
                    if not (_return:=self.__memory.get(name, {}).get(args_value)):
                        if _return:=func(*args, **kwargs):
                            if isinstance(self.__memory.get(name), dict):
                                self.__memory[name].update({args_value: _return})
                            else:
                                self.__memory[name] = {args_value: _return}
                else:
                    if not (_return:=self.__memory.get(name)):
                        if _return:=func(*args, **kwargs):
                            self.__memory = {name: _return}
                return _return
            return action
        return cache_action

