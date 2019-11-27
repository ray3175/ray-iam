from ...dao import transaction
from ...dao.project.project import DaoProjectProject


class ServiceProjectProject:
    @classmethod
    @transaction
    def add_project(cls, name, domain, logout_url, license_key, **kwargs):
        return DaoProjectProject.add_project(name, domain, logout_url, license_key, **kwargs)

