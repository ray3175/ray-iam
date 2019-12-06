from sqlalchemy import Column, String, Integer, Boolean
from ..lib.database.module import Module


class Project(Module):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, comment="项目ID")
    name = Column(String(32), nullable=False, comment="项目名称")
    domain = Column(String(64), nullable=False, comment="项目域名")
    login_url = Column(String(64), comment="登入地址")
    logout_url = Column(String(64), comment="登出地址")
    auth_code = Column(String(16), comment="授权码")
    cookie_xy_auth = Column(Boolean, default=True, comment="Cookie xy-auth 鉴权")
    header_xy_auth = Column(Boolean, default=True, comment="Header xy-auth 鉴权")
    active = Column(Boolean, default=True, comment="是否启用")

