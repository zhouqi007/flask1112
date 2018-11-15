from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()


def init_ext(app):
    se = Session()
    se.init_app(app)
    db.init_app(app)
    #实例化Migrate
    migrate = Migrate(app=app,db=db)

