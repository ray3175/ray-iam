from sqlalchemy import Column, ForeignKey, String, BigInteger, Boolean
from sqlalchemy.orm import relationship
from .. import Module


class WeChatUser(Module):
    __tablename__ = "we_chat_user"

    id = Column(BigInteger, primary_key=True, comment="微信用户ID")
    openid = Column(String(256), nullable=False, comment="微信openid")
    person_id = Column(BigInteger, ForeignKey("person.id", ondelete="SET NULL"), index=True, comment="用户ID")
    person = relationship("Person", backref="*we_chat_user_from_person*")
    xy = Column(Boolean, default=True, comment="软删除")

