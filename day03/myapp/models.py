from myapp.ext import db

class Dog(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(30),
        nullable=True,
        unique=True
    )
    place = db.Column(
        db.String(50),
        default="九堡户口"
    )
    def to_dict(self):
        data = {
            "id":self.id,
            "name":self.name,
            "place":self.place
        }
        return data

class Grade(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(20),
        nullable=True,
        unique=True
    )
    stus = db.relationship(
        "Stu",
        backref = "grade",
        lazy = True
    )


class Stu(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(20),
        nullable=True,
        unique=True
    )
    grader_id = db.Column(
        db.Integer,
        db.ForeignKey("grade.id")
    )


#多对多模型
class Tag(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    title = db.Column(
        db.String(20)
    )

tags = db.Table(
    "tags",
    db.Column("tag_id",db.Integer,db.ForeignKey("tag.id"),primary_key=True),
    db.Column("book_id",db.Integer,db.ForeignKey("book.id"),primary_key=True)

)


class Book(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(20)
    )
    #tags是指到连接的数据
    tags = db.relationship(
        "Tag",
        secondary=tags ,   #中间表
        backref=db.backref("books", lazy=True),  #反向关系 books是外面的表指回来
        lazy=True
     )


#一对多实例编写

# class Boss(db.Model):
#     id = db.Column(
#         db.Integer,
#         primary_key=True,
#         autoincrement=True
#     )
#     name = db.Column(
#         db.String(20),
#         nullable=True
#     )
#     employees = db.relationship(
#         "Employees",
#         backref = "boss",
#         lazy = True
#     )
#
# class Employees(db.Model):
#     id = db.Column(
#         db.Integer,
#         primary_key=True,
#         autoincrement=True
#     )
#     name = db.Column(
#         db.String(20),
#         nullable=True
#     )
#     boss = db.Column(
#         db.Integer,
#         db.ForeignKey("boss.id")
#     )
