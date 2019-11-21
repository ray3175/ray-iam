import redis
from ...config import AppConfig


class Redis:
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

    @classmethod
    def auth_redis_set(cls, name, value):
        return cls.auth_redis.set(name, value, ex=cls.auth_redis_config["ex"])

    @classmethod
    def auth_redis_get(cls, name):
        return cls.auth_redis.get(name)

    @classmethod
    def auth_redis_delete(cls, name):
        return cls.auth_redis.delete(name)

    @classmethod
    def user_redis_set(cls, name, value):
        return cls.user_redis.set(name, value, ex=cls.user_redis_config["ex"])

    @classmethod
    def user_redis_get(cls, name):
        return cls.user_redis.get(name)

    @classmethod
    def user_redis_delete(cls, name):
        return cls.user_redis.delete(name)

    @classmethod
    def project_redis_set(cls, name, value):
        return cls.project_redis.set(name, value, ex=cls.project_redis_config["ex"])

    @classmethod
    def project_redis_get(cls, name):
        return cls.project_redis.get(name)

    @classmethod
    def project_redis_delete(cls, name):
        return cls.project_redis.delete(name)

