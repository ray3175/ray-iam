import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool
from .modules import Module


class DB:
    def __init__(self, user, pwd, host, port, db, charset):
        self.__url = "mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}?charset={charset}".format(user=user, pwd=pwd, host=host, port=port, db=db, charset=charset)
        self.__engine = create_engine(self.__url, pool_recycle=3600, poolclass=NullPool, encoding="utf-8")
        self.__Session = scoped_session(sessionmaker(autoflush=False, bind=self.__engine))

    @property
    def session(self):
        return self.__Session()

    def init_db(self):
        Module.metadata.create_all(self.__engine)
        return True

    def drop_db(self):
        Module.metadata.drop_all(self.__engine)
        return True


