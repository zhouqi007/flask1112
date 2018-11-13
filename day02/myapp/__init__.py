from flask import Flask
from flask_session import Session


from redis import StrictRedis

from myapp.models import db
from .views.views import blue


def create_app():
    app = Flask(__name__)
    #密钥
    app.config["SECRET_KEY"] = "shibushishayawoshelemiyao"


    #指定session存储方案
    app.config["SESSION_TYPE"]="redis"
    #设置缓存开头，一般以自己pythonpoackage的app名字为开头
    app.config["SESSION_KEY_PREFIX"] = "myapp"
    # 定制化的将session存在redis的指定库中
    app.config["SESSION_REDIS"] = StrictRedis(host="127.0.0.1", db=5)


    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    #创建数据库文件
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite3.db"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123@39.108.136.163:3306/flask02"

    #实例化第三方插件
    #实例化Session
    sess = Session()
    sess.init_app(app)
    db.init_app(app)

    app.register_blueprint(blue)
    return app