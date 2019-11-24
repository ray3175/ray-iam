from functools import wraps
from ..lib.database import Dao
from ..common.logger import LoggerRun


logger = LoggerRun()


def transaction(auto_commit=True):
    def transaction_action(func):
        @wraps(func)
        def action(*args, **kwargs):
            if "__session__" not in kwargs:
                kwargs["__session__"] = Dao.Session()
                session = kwargs["__session__"]
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
            else:
                _return = func(*args, **kwargs)
                kwargs["__session__"].manual_commit |= bool(auto_commit)
            return _return
        return action
    return transaction_action(auto_commit) if callable(auto_commit) else transaction_action

