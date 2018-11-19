from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String(30),
        nullable=False,
        unique=True
    )

    age = db.Column(
        db.Integer,
        default=1
    )