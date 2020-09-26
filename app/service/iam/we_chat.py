import pickle
from ...lib.cache.redis import CacheRedis
from .. import Service


class ServiceIamWeChat(Service):
    def __init__(self):
        super().__init__()

    def get_we_chat_user_with_token(self, token):
        if we_chat_user:=CacheRedis().get_redis_info_from_redis_dict("we_chat")["redis"].get(token):
            we_chat_user = pickle.loads(we_chat_user)
        return we_chat_user

    def logout_we_chat_user_with_token(self, token):
        return CacheRedis().get_redis_info_from_redis_dict("we_chat")["redis"].delete(token)


