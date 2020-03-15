import os
import pickle


class DBConfig:
    CONFIG_PATH = os.path.dirname(os.path.abspath(__file__))
    LOCAL_DB_FILE = os.path.join(CONFIG_PATH, "LOCAL_DB")
    REMOTE_DB_FILE = os.path.join(CONFIG_PATH, "REMOTE_DB")

    def __init__(self):
        if not os.path.exists(self.CONFIG_PATH):
            os.makedirs(self.CONFIG_PATH)

    def read_local_db(self):
        config = dict(user="", pwd="", host="", port="", db="", charset="")
        if os.path.exists(self.LOCAL_DB_FILE):
            with open(self.LOCAL_DB_FILE, "rb") as x:
                config = pickle.load(x)
                x.close()
        return config

    def write_local_db(self, user, pwd, host="127.0.0.1", port="3306", db="ray_iam", charset="utf8mb4"):
        config = dict(
            user=user,
            pwd=pwd,
            host=host,
            port=port,
            db=db,
            charset=charset
        )
        with open(self.LOCAL_DB_FILE, "wb") as x:
            pickle.dump(config, x)
            x.close()
        return True

    def read_remote_db(self):
        config = dict(user="", pwd="", host="", port="", db="", charset="")
        if os.path.exists(self.REMOTE_DB_FILE):
            with open(self.REMOTE_DB_FILE, "rb") as x:
                config = pickle.load(x)
                x.close()
        return config

    def write_remote_db(self, user, pwd, host, port="3306", db="ray_iam", charset="utf8mb4"):
        config = dict(
            user=user,
            pwd=pwd,
            host=host,
            port=port,
            db=db,
            charset=charset
        )
        with open(self.REMOTE_DB_FILE, "wb") as x:
            pickle.dump(config, x)
            x.close()
        return True


