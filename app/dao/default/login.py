from ...modules.administrator import Administrator


class DaoDefaultLogin:
    @classmethod
    def get_administrator_with_account(cls, account, **kwargs):
        session = kwargs["__session__"]
        return session.query(Administrator).filter_by(account=account).first()

