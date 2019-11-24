from xy.common.global_data import GlobalData


class ServiceDefaultLogout:
    global_data = GlobalData()

    @classmethod
    def auth_verify(cls, user):
        return cls.global_data["ray-iam-auth"].pop(user, None)

