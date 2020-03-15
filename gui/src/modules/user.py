from sqlalchemy import Column, ForeignKey, String, BigInteger, Boolean
from sqlalchemy.orm import relationship
from . import Module


class User(Module):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True, comment="用户账号ID")
    account = Column(String(32), unique=True, nullable=False, comment="用户账号")
    password = Column(String(64), nullable=False, comment="用户密码")
    person_id = Column(BigInteger, ForeignKey("person.id", ondelete="SET NULL"), index=True, comment="用户ID")
    person = relationship("Person", backref="user_from_person")
    xy = Column(Boolean, default=True, comment="软删除")

    def __call__(self, *args, **kwargs):
        _return = super().__call__(*args, **kwargs)
        if kwargs.get("add_column") and "person" in kwargs["add_column"]:
            kwargs["add_column"].remove("person")
            _return.update({"person": self.person(*args, **kwargs) if self.person_id else None})
        return _return

