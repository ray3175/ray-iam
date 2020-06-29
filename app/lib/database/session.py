from functools import wraps
from flask import g
from xy.exception import XYException
from ...common.logger import LoggerRun
from ...dao import Dao
from . import DB


class Session(DB):
    @classmethod
    def _if_dao_set_session(cls, self, session):
        if isinstance(self.dao, Dao):
            self.dao.session = session

    @classmethod
    def transaction(cls, auto_commit=True):
        logger = LoggerRun()
        def transaction_action(func):
            @wraps(func)
            def action(*args, **kwargs):
                self = args[0]
                if db_session:=g.get("__db_session__"):
                    cls._if_dao_set_session(self, db_session)
                    _return = func(*args, **kwargs)
                    db_session.__commit__ |= bool(auto_commit)
                else:
                    db_session = g.__db_session__ = cls.Session()
                    db_session.__commit__ = bool(auto_commit)
                    cls._if_dao_set_session(self, db_session)
                    try:
                        _return = func(*args, **kwargs)
                        if db_session.__commit__:
                            db_session.commit()
                    except Exception as e:
                        logger.error(f"数据库事务出现异常！\nerror：\n{e}")
                        db_session.rollback()
                        raise XYException("数据库事务出现异常，详情见日志！")
                    finally:
                        db_session.close()
                        g.pop("__db_session__")
                return _return
            return action
        return transaction_action(auto_commit) if callable(auto_commit) else transaction_action

