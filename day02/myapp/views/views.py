from flask import Blueprint, session, render_template
from jinja2 import Template

from myapp.models import db

from myapp.models import Person

blue = Blueprint("day02",__name__)



@blue.route("/set")
def set():
    session["hehe"] = "xixi"
    return "ok"

@blue.route("/get")
def get():
    return session.get("hehe","not set")

@blue.route("/index")
def index():
    #加载
    import os
    #获取当前文件所在的路径
    # root = os.path.dirname(__file__)
    # print(root)
    file_path = os.path.join("/home/zhouqi/flask/day02/myapp","templates","index.html")
    file = open(file_path,"r")
    template = Template(file.read())
    #渲染
    html = template.render()
    return html

#模板的继承
@blue.route("/block")
def my_block():
    return render_template("test.html")

#宏定义，可以在模板中定义函数，在其它地方调用
@blue.route("/my_macro")
def my_marco():
    data = ["pathon","pHp","c","  hehhe  xixiix","hello nice to"]
    return render_template("my_marco.html",data=data)

#创建数据表
@blue.route("/create")
def create_db():
    db.create_all()
    return "创建完毕"

@blue.route("/drop")
def drop_db():
    db.drop_all()
    return "删除完毕"

#创建数据
@blue.route("/create_data")
def create_user():
    #创建数据
    # u = Person(
    #     name = "张三"
    # )
    # #保存到数据库
    # db.session.add(u)

    #批量创建
    persons = []
    for i in range(10):
        u  = Person(
            name = "张三" + str(i)
        )
        persons.append(u)
    db.session.add_all(persons)
    db.session.commit()
    return "创建完毕"

@blue.route("/get_users")
def get_users():
    res = Person.query.all()
    for i in res:
        print(i.name)

    return "ok"