from ..lib.database.base import Base
from ..lib.database import Dao


class InitDB(Dao):
    def create_db(self):
        """
        如果没有创建数据库，先执行下列命令创建数据库：
            create database ray_iam default charset utf8mb4;
        """
        from .. import modules
        Base.metadata.create_all(self.engine)

    def drop_db(self):
        from .. import modules
        Base.metadata.drop_all(self.engine)

    def add_administrator(self):
        from ..modules.administrator import Administrator
        administrator = Administrator(account="qq57464715",
                                      password="123456",
                                      auth=99)
        session = self.Session()
        session.add(administrator)
        session.commit()
        session.close()

