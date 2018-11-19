from flask import Flask

from myapp.ext import init_ext
from myapp.settings import conf
# from myapp.views import init_blue
from myapp.urls_apis_v1 import init_api


def create_app(env_name):
    #实例化app
    app = Flask(__name__)
    #配置
    app.config.from_object(conf.get(env_name))
    #实例化第三方插件
    init_ext(app)

    init_api(app)
    #注册蓝图
    # init_blue(app)
    return app