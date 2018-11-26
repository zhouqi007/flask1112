from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_bootstraps import Bootstrap
from flask_mail import Mail
from flask_caching import Cache

from myapp.settings import CACHE

db = SQLAlchemy()
# bootstrap = Bootstrap()
mail = Mail()
cache =Cache()
def init_ext(app):
    migrate = Migrate(app=app,db=db)
    se = Session()
    se.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    cache.init_app(app,{"CACHE_TYPE":"redis"})
    # bootstrap.init_app(app)




