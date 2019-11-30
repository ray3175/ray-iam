from xy.common.global_data import GlobalData


class ServiceDefaultLogout:
    global_data = GlobalData()

    def auth_verify(self, user):
        return self.global_data["ray-iam-auth"].pop(user, None)

