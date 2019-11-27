from ...modules.project import Project


class DaoProjectProject:
    @classmethod
    def add_project(cls, name, domain, logout_url, license_key, **kwargs):
        session = kwargs["__session__"]
        project = Project(name=name,
                          domain=domain,
                          logout_url=logout_url,
                          license_key=license_key)
        session.add(project)
        return True

