from abc import ABC, abstractmethod
import redis
from ...config import AppConfig


class Redis(ABC):
    redis_config = AppConfig()["cache"]["redis"]
    user_redis_config = redis_config["user-db"]
    user_pool = redis.ConnectionPool(password=redis_config["password"], host=redis_config["host"], port=redis_config["port"], db=user_redis_config["db"])
    user_redis = redis.Redis(connection_pool=user_pool)

    @abstractmethod
    def cache_redis(self, name, args_name, serial=True):
        pass

