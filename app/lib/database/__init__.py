from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool
from xy.common.global_data import GlobalData
from ...config import AppConfig


class Dao:
    url = "{scheme}://{user}:{password}@{host}:{port}/{db}?charset={charset}".format(**AppConfig()[GlobalData().get("environment", "environment-development")]["database"])
    engine = create_engine(url, pool_recycle=3600, poolclass=NullPool, encoding="utf-8")
    Session = scoped_session(sessionmaker(autoflush=False, bind=engine))

