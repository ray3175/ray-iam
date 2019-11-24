from functools import wraps
from ...config import AppConfig
from .redis import Redis


class Cache(Redis):
    if AppConfig()["cache"]["serialize"] == "json":
        import json
        serialize = json
    else:
        import pickle
        serialize = pickle

    @classmethod
    def cache_redis(cls, name, args_name, serial=True):
        _redis = getattr(cls, f"{name}_redis")
        def cache_action(func):
            @wraps(func)
            def action(*args, **kwargs):
                args_value = args[co_varnames.index(args_name)] if (co_varnames:=func.__code__.co_varnames) and args_name in co_varnames else kwargs.get(args_name)
                if _return:=_redis.get(args_value):
                    if serial:
                        _return = cls.serialize.loads(_return)
                else:
                    if _return:=func(*args, **kwargs):
                        _redis.set(args_value, cls.serialize.dumps(_return) if serial else _return, ex=getattr(cls, f"{name}_redis_config")["ex"])
                return _return
            return action
        return cache_action

