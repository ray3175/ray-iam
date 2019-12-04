from sqlalchemy import Column, String, BigInteger, Boolean
from ..lib.database.module import Module


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
        _return = super().__call__()
        _return.update({
            "phone": [i() for i in self.phone_from_person],
            "mail": [i() for i in self.mail_from_person]
        })
        return _return

