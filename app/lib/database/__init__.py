from functools import wraps
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool
from ...config import AppConfig
from ...common.logger import LoggerRun


class DB:
    url = "{scheme}://{user}:{password}@{host}:{port}/{db}?charset={charset}".format(**AppConfig()["database"])
    engine = create_engine(url, pool_recycle=3600, poolclass=NullPool, encoding="utf-8")
    Session = scoped_session(sessionmaker(autoflush=False, bind=engine))

    @classmethod
    def transaction(cls, auto_commit=True):
        logger = LoggerRun()
        def transaction_action(func):
            @wraps(func)
            def action(*args, **kwargs):
                self = args[0]
                if "__session__" in kwargs:
                    self.dao.session = kwargs["__session__"]
                    _return = func(*args, **kwargs)
                    self.dao.session.manual_commit |= bool(auto_commit)
                else:
                    session = self.dao.session = kwargs["__session__"] = cls.Session()
                    session.manual_commit = bool(auto_commit)
                    try:
                        _return = func(*args, **kwargs)
                        if session.manual_commit:
                            session.commit()
                    except Exception as e:
                        logger.error(f"数据库事务出现异常！\nerror：\n{e}")
                        session.rollback()
                        _return = False
                    finally:
                        session.close()
                return _return
            return action
        return transaction_action(auto_commit) if callable(auto_commit) else transaction_action

    @classmethod
    def session(cls, func):
        @wraps(func)
        def set_session(*args, **kwargs):
            if not args[0].session:
                args[0].session = cls.Session()
            return func(*args, **kwargs)
        return set_session

