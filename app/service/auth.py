from xy.common.global_data import GlobalData


class ServiceAuth:
    global_data = GlobalData()

    def ray_iam_auth(self, user, password):
        return password and password == self.global_data["ray-iam-auth"].get(user)
