from sqlalchemy import Column, String, BigInteger, Boolean
from . import Module


class Person(Module):
    __tablename__ = "person"

    id = Column(BigInteger, primary_key=True, comment="用户ID")
    id_card = Column(String(32), unique=True, nullable=False, comment="用户身份证")
    name = Column(String(32), comment="用户姓名")
    sex = Column(String(8), comment="用户性别")
    birth_date = Column(String(16), comment="用户出生年月日")
    birth_place = Column(String(64), comment="出生地")
    native_place = Column(String(32), comment="籍贯")
    nationality = Column(String(32), comment="名族")
    xy = Column(Boolean, default=True, comment="软删除")

    def __call__(self, *args, **kwargs):
        _return = super().__call__(*args, **kwargs)
        if kwargs.get("add_column"):
            if "user" in kwargs["add_column"]:
                kwargs["add_column"].remove("user")
                _return.update({"user": [i(*args, **kwargs) for i in self.user_from_person]})
            if "phone" in kwargs["add_column"]:
                kwargs["add_column"].remove("phone")
                _return.update({"phone": [i(*args, **kwargs) for i in self.phone_from_person]})
            if "mail" in kwargs["add_column"]:
                kwargs["add_column"].remove("mail")
                _return.update({"mail": [i(*args, **kwargs) for i in self.mail_from_person]})
            if "we_chat_user" in kwargs["add_column"]:
                kwargs["add_column"].remove("we_chat_user")
                _return.update({"we_chat_user": [i(*args, **kwargs) for i in self.we_chat_user_from_person]})
        return _return

