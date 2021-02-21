from ..lib.database.module import Module
from ..lib.database import DB


class InitDB(DB):
    def create_database(self):
        connection = DB.engine.connect()
        connection.execute("create database if not exists ray_sso default charset utf8mb4;")

    def create_db(self):
        from .. import modules
        self.create_database()
        Module.metadata.create_all(self.engine_db)

    def drop_db(self):
        from .. import modules
        Module.metadata.drop_all(self.engine_db)

    def add_administrator(self):
        from ..modules.administrator import Administrator
        administrator = Administrator(account="qq57464715",
                                      password="123456",
                                      auth=99)
        session = self.Session()
        session.add(administrator)
        session.commit()
        session.close()

