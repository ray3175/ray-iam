from sqlalchemy import Column, ForeignKey, String, BigInteger, Boolean
from sqlalchemy.orm import relationship
from ..lib.database.base import Base


class Phone(Base):
    __tablename__ = "phone"

    id = Column(BigInteger, primary_key=True, comment="用户手机号ID")
    phone = Column(String(32), comment="用户手机号")
    person_id = Column(BigInteger, ForeignKey("person.id", ondelete="CASCADE"), index=True, comment="用户ID")
    person = relationship("Person", backref="phone_from_person")
    xy = Column(Boolean, default=True, comment="软删除")

