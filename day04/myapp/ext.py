from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_bootstraps import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_caching import Cache

from myapp.settings import CACHE

db = SQLAlchemy()
bootstrap = Bootstrap()
cache = Cache()

def init_ext(app):
    migrate = Migrate(app=app,db=db)
    se = Session()
    se.init_app(app)
    db.init_app(app)

    # 调试插件的实例化
    debug = DebugToolbarExtension()
    debug.init_app(app)
    #缓存
    cache.init_app(app,config=CACHE.get("default"))

    bootstrap.init_app(app)




