import redis
from xy.common.global_data import GlobalData
from ...config import AppConfig


class Redis:
    redis_config = AppConfig()[GlobalData().get("environment", "environment-development")]["cache"]["redis"]
    auth_redis_config = redis_config["auth-db"]
    user_redis_config = redis_config["user-db"]
    auth_pool = redis.ConnectionPool(password=redis_config["password"], host=redis_config["host"], port=redis_config["port"], db=auth_redis_config["db"], decode_responses=True)
    auth_redis = redis.Redis(connection_pool=auth_pool)
    user_pool = redis.ConnectionPool(password=redis_config["password"], host=redis_config["host"], port=redis_config["port"], db=user_redis_config["db"])
    user_redis = redis.Redis(connection_pool=user_pool)

    @classmethod
    def auth_redis_set(cls, name, value):
        return cls.auth_redis.set(name, value, ex=cls.auth_redis_config["ex"], px=cls.auth_redis_config["px"], nx=cls.auth_redis_config["nx"], xx=cls.auth_redis_config["xx"])

    @classmethod
    def auth_redis_get(cls, name):
        return cls.auth_redis.get(name)

    @classmethod
    def auth_redis_delete(cls, name):
        return cls.auth_redis.delete(name)

    @classmethod
    def user_redis_set(cls, name, value):
        return cls.user_redis.set(name, value, ex=cls.user_redis_config["ex"], px=cls.user_redis_config["px"], nx=cls.user_redis_config["nx"], xx=cls.user_redis_config["xx"])

    @classmethod
    def user_redis_get(cls, name):
        return cls.user_redis.get(name)

    @classmethod
    def user_redis_delete(cls, name):
        return cls.user_redis.delete(name)

