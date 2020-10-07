from xy.exception import XYException
from ... import app
from .response import response
from .redirect import redirect_to_source


class Errorhandler:
    @staticmethod
    @app.errorhandler(400)
    def error_400(error):
        return response(400, msg="参数有误！")

    @staticmethod
    @app.errorhandler(401)
    def error_401(error):
        return response(401, msg="无效的权限！")

    @staticmethod
    @app.errorhandler(404)
    def error_404(error):
        return redirect_to_source("./common/error404.html")

    @staticmethod
    @app.errorhandler(XYException)
    def error_xy(error):
        return response(code=500, msg=error.msg)

