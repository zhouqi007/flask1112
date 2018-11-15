from flask import Flask

from myapp.ext import init_ext
from myapp.settings import conf
from myapp.views import blue, init_blue


def create_app(env_name):
    #实例化
    app = Flask(__name__)
    #配置
    app.config.from_object(conf.get(env_name,"debug"))
    #实例化第三方
    init_ext(app)
    #注册蓝图
    init_blue(app)
    return app