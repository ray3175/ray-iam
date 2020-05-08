from abc import ABC, abstractmethod


class Cache(ABC):
    def _extract_args_value(self, func, args_name, *args, **kwargs):
        return args[co_varnames.index(args_name)] if (co_varnames:=func.__code__.co_varnames) and args_name in co_varnames else kwargs.get(args_name)

    @abstractmethod
    def cache(self, name, args_name, *args, **kwargs):
        pass

