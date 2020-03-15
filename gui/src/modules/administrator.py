from sqlalchemy import Column, String, Integer, SmallInteger, Text
from . import Module


class Administrator(Module):
    __tablename__ = "administrator"

    id = Column(Integer, primary_key=True, comment="管理员ID")
    account = Column(String(16), unique=True, nullable=False, comment="管理员账号")
    password = Column(String(32), nullable=False, comment="管理员密码")
    auth = Column(SmallInteger, default=0, comment="管理员权限")
    remark = Column(Text, comment="备注")

