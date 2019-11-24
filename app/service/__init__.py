from xy.common.global_data import GlobalData


class Service:
    global_data = GlobalData()

    @classmethod
    def ray_iam_auth(cls, user, password):
        return password and password == cls.global_data["ray-iam-auth"].get(user)
