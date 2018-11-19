from flask_restful import Api
from myapp.apis_v1 import *
api = Api()

def init_api(app):
    api.init_app(app)

# 下面注册各种路由


api.add_resource(NewsOneApi,"/newsone")
api.add_resource(TwoApi,"/two")
api.add_resource(ThreeApi,"/three/<int:id>")
api.add_resource(FourApi,"/four/<int:page>/<int:per_page>")
api.add_resource(FiveApi,"/five")
api.add_resource(TestAPI,"/test")
