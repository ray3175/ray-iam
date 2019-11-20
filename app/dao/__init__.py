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
                try:
                    _return = func(*args, **kwargs)
                    if auto_commit:
                        session.commit()
                except Exception as e:
                    logger.error(f"数据库事务出现异常！\nerror：\n{e}")
                    session.rollback()
                    _return = False
                finally:
                    session.close()
            else:
                _return = func(*args, **kwargs)
            return _return
        return action
    return transaction_action(auto_commit) if callable(auto_commit) else transaction_action

