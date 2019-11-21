from sqlalchemy import Column, String, Integer, Boolean
from ..lib.database.base import Base


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, comment="项目ID")
    name = Column(String(32), comment="项目名称")
    domain = Column(String(64), comment="项目域名")
    active = Column(Boolean, default=True, comment="启用")

