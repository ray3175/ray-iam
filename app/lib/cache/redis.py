from functools import wraps
import redis
from xy.decorator.singleton import Singleton
from xy.exception import XYException
from ...config import AppConfig
from . import Cache


@Singleton
class CacheRedis(Cache):
    def __init__(self):
        if AppConfig()["cache"]["serialize"] == "json":
            import json
            self.__serialize = json
        else:
            import pickle
            self.__serialize = pickle
            self.__init_redis()

    def __init_redis(self):
        redis_config = AppConfig()["cache"]["redis"]
        self.__project_redis_config = redis_config["project-db"]
        self.__project_pool = redis.ConnectionPool(password=redis_config["password"], host=redis_config["host"], port=redis_config["port"], db=self.__project_redis_config["db"])
        self.__project_redis = redis.Redis(connection_pool=self.__project_pool)
        self.__auth_redis_config = redis_config["auth-db"]
        self.__auth_pool = redis.ConnectionPool(password=redis_config["password"], host=redis_config["host"], port=redis_config["port"], db=self.__auth_redis_config["db"])
        self.__auth_redis = redis.Redis(connection_pool=self.__auth_pool)
        self.__we_chat_redis_config = redis_config["we-chat-db"]
        self.__we_chat_pool = redis.ConnectionPool(password=redis_config["password"], host=redis_config["host"], port=redis_config["port"], db=self.__we_chat_redis_config["db"])
        self.__we_chat_redis = redis.Redis(connection_pool=self.__we_chat_pool)

    @property
    def project_redis_config(self):
        return self.__project_redis_config

    @property
    def auth_redis_config(self):
        return self.__auth_redis_config

    @property
    def we_chat_redis_config(self):
        return self.__we_chat_redis_config

    @property
    def project_redis(self):
        return self.__project_redis

    @property
    def auth_redis(self):
        return self.__auth_redis

    @property
    def we_chat_redis(self):
        return self.__we_chat_redis

    def cache(self, name, args_name, serial=True, *args, **kwargs):
        """
        :param name: redis连接池名称，如：project
        :param args_name: 作为 key 的参数名称
        :param serial: 是否序列化
        """
        _redis = getattr(self, f"{name}_redis")
        def cache_action(func):
            @wraps(func)
            def action(*args, **kwargs):
                args_value = self._extract_args_value(func, args_name, *args, **kwargs)
                try:
                    _return = _redis.get(args_value)
                except redis.exceptions.ConnectionError:
                    _return = None
                except Exception as e:
                    raise XYException(f"Redis服务出现异常！\n\t{e}")
                if _return:
                    if serial:
                        _return = self.__serialize.loads(_return)
                else:
                    if _return:=func(*args, **kwargs):
                        try:
                            _redis.set(args_value, self.__serialize.dumps(_return) if serial else _return, ex=getattr(self, f"{name}_redis_config")["ex"])
                        except redis.exceptions.ConnectionError:
                            pass
                        except Exception as e:
                            raise XYException(f"Redis服务出现异常！\n\t{e}")
                return _return
            return action
        return cache_action

