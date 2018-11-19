from myapp.ext import db


class News(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    title = db.Column(
        db.String(30),
        index=True
    )
    content = db.Column(
        db.String(100),
        nullable=True
    )
    type = db.Column(
        db.String(30),
        default="军事"
    )

    def to_dict(self):
        data = {
            "id":self.id,
            "title":self.title,
            "content":self.content,
            "type":self.type
        }
        return data