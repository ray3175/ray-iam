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
    def cache_auth_redis(cls, name):
        def cache_action(func):
            @wraps(func)
            def action(*args, **kwargs):
                if not (_return:=cls.auth_redis_get(name)):
                    if _return:=func(*args, **kwargs):
                        cls.auth_redis_set(name, _return)
                return _return
            return action
        return cache_action

    @classmethod
    def cache_user_redis(cls, name):
        def cache_action(func):
            @wraps(func)
            def action(*args, **kwargs):
                if _return:=cls.user_redis_get(name):
                    _return = cls.serialize.loads(_return)
                else:
                    if _return:=func(*args, **kwargs):
                        cls.user_redis_set(name, cls.serialize.dumps(_return))
                return _return
            return action
        return cache_action

    @classmethod
    def cache_project_redis(cls, name):
        def cache_action(func):
            @wraps(func)
            def action(*args, **kwargs):
                if _return:=cls.project_redis_get(name):
                    _return = cls.serialize.loads(_return)
                else:
                    if _return:=func(*args, **kwargs):
                        cls.project_redis_set(name, cls.serialize.dumps(_return))
                return _return
            return action
        return cache_action

