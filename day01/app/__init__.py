from flask import Flask
from .views import blue
def create_app():
    #创建app
    app = Flask(__name__)
    #使用session时需要配置的，相当于密码
    app.config["SECRET_KEY"]="guanfangyidianerde"
    #注册蓝图
    app.register_blueprint(blue)
    return app