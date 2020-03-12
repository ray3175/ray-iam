from abc import ABC, abstractmethod
import redis
from ...config import AppConfig


class Redis(ABC):
    redis_config = AppConfig()["cache"]["redis"]
    auth_redis_config = redis_config["auth-db"]
    auth_pool = redis.ConnectionPool(password=redis_config["password"], host=redis_config["host"], port=redis_config["port"], db=auth_redis_config["db"])
    auth_redis = redis.Redis(connection_pool=auth_pool)
    we_chat_redis_config = redis_config["we-chat-db"]
    we_chat_pool = redis.ConnectionPool(password=redis_config["password"], host=redis_config["host"], port=redis_config["port"], db=we_chat_redis_config["db"])
    we_chat_redis = redis.Redis(connection_pool=we_chat_pool)

    @abstractmethod
    def cache_redis(self, name, args_name, serial=True):
        pass

