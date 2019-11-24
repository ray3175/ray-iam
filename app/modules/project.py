from sqlalchemy import Column, String, Integer, Boolean
from ..lib.database.base import Base


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, comment="项目ID")
    name = Column(String(32), comment="项目名称")
    domain = Column(String(64), comment="项目域名")
    logout_url = Column(String(64), comment="注销地址")
    license_key = Column(String(16), comment="授权码")
    active = Column(Boolean, default=True, comment="是否启用")

