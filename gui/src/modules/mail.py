from sqlalchemy import Column, ForeignKey, String, BigInteger, Boolean
from sqlalchemy.orm import relationship
from . import Module


class Mail(Module):
    __tablename__ = "mail"

    id = Column(BigInteger, primary_key=True, comment="用户邮箱ID")
    mail = Column(String(128), comment="用户邮箱")
    person_id = Column(BigInteger, ForeignKey("person.id", ondelete="CASCADE"), index=True, nullable=False, comment="用户ID")
    person = relationship("Person", backref="mail_from_person")
    xy = Column(Boolean, default=True, comment="软删除")

    def __call__(self, *args, **kwargs):
        _return = super().__call__(*args, **kwargs)
        if kwargs.get("add_column") and "person" in kwargs["add_column"]:
            kwargs["add_column"].remove("person")
            _return.update({"person": self.person(*args, **kwargs)})
        return _return

