from abc import ABC, abstractmethod
import redis
from ...config import AppConfig


class Redis(ABC):
    redis_config = AppConfig()["cache"]["redis"]
    auth_redis_config = redis_config["auth-db"]
    user_redis_config = redis_config["user-db"]
    project_redis_config = redis_config["project-db"]
    auth_pool = redis.ConnectionPool(password=redis_config["password"], host=redis_config["host"], port=redis_config["port"], db=auth_redis_config["db"], decode_responses=True)
    auth_redis = redis.Redis(connection_pool=auth_pool)
    user_pool = redis.ConnectionPool(password=redis_config["password"], host=redis_config["host"], port=redis_config["port"], db=user_redis_config["db"])
    user_redis = redis.Redis(connection_pool=user_pool)
    project_pool = redis.ConnectionPool(password=redis_config["password"], host=redis_config["host"], port=redis_config["port"], db=project_redis_config["db"])
    project_redis = redis.Redis(connection_pool=project_pool)

    @abstractmethod
    def cache_redis(self, name, args_name, serial=True):
        pass

