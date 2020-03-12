from sqlalchemy import Column, ForeignKey, String, BigInteger, Boolean
from sqlalchemy.orm import relationship
from ...lib.database.module import Module


class WeChatUser(Module):
    __tablename__ = "we_chat_user"

    id = Column(BigInteger, primary_key=True, comment="微信用户ID")
    openid = Column(String(256), index=True, nullable=False, comment="微信openid")
    person_id = Column(BigInteger, ForeignKey("person.id", ondelete="SET NULL"), index=True, comment="用户ID")
    person = relationship("Person", backref="we_chat_user_from_person")
    xy = Column(Boolean, default=True, comment="软删除")

    def __call__(self, *args, **kwargs):
        _return = super().__call__(*args, **kwargs)
        if kwargs.get("add_column") and "person" in kwargs["add_column"]:
            kwargs["add_column"].remove("person")
            _return.update({"person": self.person(*args, **kwargs) if self.person_id else None})
        return _return

