import time
from .config import DBConfig
from .modules.administrator import Administrator
from .modules.project import Project
from .modules.person import Person
from .modules.user import User
from .modules.phone import Phone
from .modules.mail import Mail
from .modules.we_chat.user import WeChatUser
from .db import DB


class Action:
    DB_MODULES = [
        {
            "name": "RayIam管理员",
            "module": Administrator
        },
        {
            "name": "项目",
            "module": Project
        },
        {
            "name": "身份信息",
            "module": Person
        },
        {
            "name": "用户",
            "module": User
        },
        {
            "name": "手机号",
            "module": Phone
        },
        {
            "name": "邮箱",
            "module": Mail
        },
        {
            "name": "微信用户",
            "module": WeChatUser
        }
    ]

    def __init__(self):
        self.__db_config = DBConfig()

    def set_local_db_config(self, user, pwd, host="127.0.0.1", port="3306", db="ray_iam", charset="utf8mb4"):
        return self.__db_config.write_local_db(user, pwd, host, port, db, charset)

    def get_local_db_config(self):
        return self.__db_config.read_local_db()

    def set_remote_db_config(self, user, pwd, host, port="3306", db="ray_iam", charset="utf8mb4"):
        return self.__db_config.write_remote_db(user, pwd, host, port, db, charset)

    def get_remote_db_config(self):
        return self.__db_config.read_remote_db()

    def init_local_db(self):
        return DB(**self.__db_config.read_local_db()).init_db()

    def drop_local_db(self):
        return DB(**self.__db_config.read_local_db()).drop_db()

    def clear_local_db(self):
        self.drop_local_db()
        self.init_local_db()

    def init_remote_db(self):
        return DB(**self.__db_config.read_remote_db()).init_db()

    def drop_remote_db(self):
        return DB(**self.__db_config.read_remote_db()).drop_db()

    def clear_remote_db(self):
        self.drop_remote_db()
        self.init_remote_db()

    def _call_func(self, func, msg):
        if func:
            func(msg)
        return True

    def _timer_run(self, func, run):
        s = time.time()
        run()
        e = time.time()
        self._call_func(func, "耗时：{}".format(e - s))
        return True

    def _db_data_migrate(self, session_read, session_write, func):
        for db_module in self.DB_MODULES:
            name = db_module["name"]
            module = db_module["module"]
            self._call_func(func, "开始迁移 {} 数据。".format(name))
            def active():
                module_list = [module(**i()) for i in session_read.query(module).all()]
                session_write.add_all(module_list)
                session_write.commit()
            self._timer_run(func, active)
        return True

    def db_data_remote2local(self, func=None):
        def recall():
            def active():
                self._call_func(func, "开始清理本地数据库！")
                self._timer_run(func, self.clear_local_db)
                session_read = DB(**self.__db_config.read_remote_db()).session
                session_write = DB(**self.__db_config.read_local_db()).session
                self._db_data_migrate(session_read, session_write, func)
                return True
            active()
            self._call_func(func, "已成功将数据从远程数据库迁移至本地！")
            return True
        self._timer_run(func, recall)
        return True

    def db_data_local2remote(self, func=None):
        def recall():
            def active():
                self._call_func(func, "开始清理远程数据库！")
                self._timer_run(func, self.clear_remote_db)
                session_read = DB(**self.__db_config.read_local_db()).session
                session_write = DB(**self.__db_config.read_remote_db()).session
                self._db_data_migrate(session_read, session_write, func)
                return True
            active()
            self._call_func(func, "已成功将数据从本地数据库迁移至远程服务器！")
            return True
        self._timer_run(func, recall)
        return True


