from functools import wraps
from ...config import AppConfig
from .memory import Memory
from .redis import Redis


class Cache(Memory, Redis):
    if AppConfig()["cache"]["serialize"] == "json":
        import json
        serialize = json
    else:
        import pickle
        serialize = pickle

    @classmethod
    def _extract_args_value(cls, func, args_name, *args, **kwargs):
        return args[co_varnames.index(args_name)] if (co_varnames:=func.__code__.co_varnames) and args_name in co_varnames else kwargs.get(args_name)

    @classmethod
    def cache_memory(cls, name, args_name=None):
        def cache_action(func):
            @wraps(func)
            def action(*args, **kwargs):
                if args_value:=cls._extract_args_value(func, args_name, *args, **kwargs) if args_name else None:
                    if not (_return:=cls.memory.get(name, {}).get(args_value)):
                        if _return:=func(*args, **kwargs):
                            if isinstance(cls.memory.get(name), dict):
                                cls.memory[name].update({args_value: _return})
                            else:
                                cls.memory[name] = {args_value: _return}
                else:
                    if not (_return:=cls.memory.get(name)):
                        if _return:=func(*args, **kwargs):
                            cls.memory = {name: _return}
                return _return
            return action
        return cache_action

    @classmethod
    def cache_redis(cls, name, args_name, serial=True):
        _redis = getattr(cls, f"{name}_redis")
        def cache_action(func):
            @wraps(func)
            def action(*args, **kwargs):
                args_value = cls._extract_args_value(func, args_name, *args, **kwargs)
                if _return:=_redis.get(args_value):
                    if serial:
                        _return = cls.serialize.loads(_return)
                else:
                    if _return:=func(*args, **kwargs):
                        _redis.set(args_value, cls.serialize.dumps(_return) if serial else _return, ex=getattr(cls, f"{name}_redis_config")["ex"])
                return _return
            return action
        return cache_action

