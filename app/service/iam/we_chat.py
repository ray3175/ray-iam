import pickle
from ...lib.cache import Cache
from .. import Service


class ServiceIamWeChat(Service):
    def __init__(self):
        super().__init__()

    def get_we_chat_user_with_token(self, token):
        if we_chat_user:=Cache.we_chat_redis.get(token):
            we_chat_user = pickle.loads(we_chat_user)
        return we_chat_user

    def logout_we_chat_user_with_token(self, token):
        return Cache.we_chat_redis.delete(token)


