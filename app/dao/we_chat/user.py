from ...modules.we_chat.user import WeChatUser
from .. import Dao


class DaoWeChatUser(Dao):
    def __init__(self, module=WeChatUser):
        super().__init__(module)

    def get_we_chat_user(self, _id):
        return self.session.query(self.module).filter_by(id=_id).first()

    def get_we_chat_user_with_openid(self, openid, xy=True):
        return self.session.query(self.module).filter(self.module.openid == openid, self.module.xy == xy).first()

