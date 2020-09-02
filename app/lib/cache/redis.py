from functools import wraps
import redis
from xy.decorator.singleton import Singleton
from xy.exception import XYException
from ...config import AppConfig
from . import Cache


@Singleton
class CacheRedis(Cache):
    def __init__(self):
        if AppConfig().cache["serialize"] == "json":
            import json
            self.__serialize = json
        else:
            import pickle
            self.__serialize = pickle
        self.__init_redis()

    def __init_redis(self):
        self.__redis_dict = dict()
        redis_config = AppConfig().cache["redis"]
        project_config = redis_config["project-db"]
        project_pool = redis.ConnectionPool(password=redis_config["password"], host=redis_config["host"], port=redis_config["port"], db=project_config["db"])
        project_redis = redis.Redis(connection_pool=project_pool)
        auth_config = redis_config["auth-db"]
        auth_pool = redis.ConnectionPool(password=redis_config["password"], host=redis_config["host"], port=redis_config["port"], db=auth_config["db"])
        auth_redis = redis.Redis(connection_pool=auth_pool)
        we_chat_config = redis_config["we-chat-db"]
        we_chat_pool = redis.ConnectionPool(password=redis_config["password"], host=redis_config["host"], port=redis_config["port"], db=we_chat_config["db"])
        we_chat_redis = redis.Redis(connection_pool=we_chat_pool)
        self.__redis_dict["project"] = dict(config=project_config, pool=project_pool, redis=project_redis)
        self.__redis_dict["auth"] = dict(config=auth_config, pool=auth_pool, redis=auth_redis)
        self.__redis_dict["we_chat"] = dict(config=we_chat_config, pool=we_chat_pool, redis=we_chat_redis)

    def cache(self, name, args_name, serial=True, *args, **kwargs):
        """
        :param name: redis连接池名称，如：project
        :param args_name: 作为 key 的参数名称
        :param serial: 是否序列化
        """
        _redis = self.__redis_dict[name]["redis"]
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
                            _redis.set(args_value, self.__serialize.dumps(_return) if serial else _return, ex=self.__redis_dict[name]["config"]["ex"])
                        except redis.exceptions.ConnectionError:
                            pass
                        except Exception as e:
                            raise XYException(f"Redis服务出现异常！\n\t{e}")
                return _return
            return action
        return cache_action

