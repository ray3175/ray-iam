from sqlalchemy import Column, ForeignKey, String, BigInteger, DateTime, Boolean
from sqlalchemy.orm import relationship
from ..lib.database.module import Module


class User(Module):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True, comment="用户账号ID")
    account = Column(String(32), unique=True, nullable=False, comment="用户账号")
    password = Column(String(64), nullable=False, comment="用户密码")
    person_id = Column(BigInteger, ForeignKey("person.id", ondelete="SET NULL"), index=True, comment="用户ID")
    person = relationship("Person", backref="*user_from_person*")
    register_time = Column(DateTime, comment="注册时间")
    xy = Column(Boolean, default=True, comment="软删除")

