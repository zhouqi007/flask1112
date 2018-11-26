from flask_restful import Api
from myapp.apis import RegisterAPI, UpdateAPI, Statu_UpdateAPI

api = Api()

def init_api(app):
    api.init_app(app)

# 下面注册各种路由
api.add_resource(RegisterAPI,"/api/register")
api.add_resource(UpdateAPI,"/api/updates")
api.add_resource(Statu_UpdateAPI,"/api/statu_update")

