from flask import Blueprint, request, render_template, jsonify
from sqlalchemy import or_

from myapp.models import *

blue = Blueprint("day03",__name__)
#注册蓝图
def init_blue(app):
    app.register_blueprint(blue)

@blue.route("/create_dog")
def create_dog():
    dogs = []
    for i in range(50):
        dog = Dog(
            name = "泰迪" + str(i),
            place = "九堡{num}户".format(num=i+1)
        )
        dogs.append(dog)
    #添加到数据库的session
    db.session.add_all(dogs)
    db.session.commit()
    return "创建成功"


#删除数据
@blue.route("/del/<int:id>")
def del_dog(id):
    dog = Dog.query.filter_by(id=id).first_or_404()
    #删除
    db.session.delete(dog)
    db.session.commit()
    return "ok"

@blue.route("/get_dogs/")
def get_dogs():
    params = request.args
    #查找id 大于20的
    # dogs = Dog.query.filter(Dog.id.__gt__(20))

    #用filter查找用的是双等号
    # dogs = Dog.query.filter(Dog.name == "泰迪9")


    #contains 包含
    # dogs = Dog.query.filter(Dog.name.contains("9"))

    #in_(条件列表) 查询在条件列表中的数据
    # dogs = Dog.query.filter(Dog.id.in_([10,12,15]))

    #like()  查询名字以9结尾的数据  %代替很多  _为一个
    dogs = Dog.query.filter(Dog.name.like("%9"))

    #get()  只能通过主键查询  get_or_404()搜索不到就返回404
    # dogs = Dog.query.get_or_404(3)
    # print(dogs)
    # return "ok"

    #offset(n)  跳过n条数据
    # dogs = dogs.offset(2)

    #limit(n) 最多拿n条数据
    # dogs = dogs.limit(3)

    #联合使用 查询集.offset(n).limit(m)，跳过n个，再最多取m个    使用顺序没关系
    # dogs = dogs.offset(2).limit(2)

    #order_by()排序，默认升序，添加负号是降序    使用order_by()后可以执行offset和limit，但是执行offset和offset后不可以使用order_by()
    dogs = dogs.order_by("-id")

    return render_template("datas.html",dogs=dogs)


@blue.route("/page/")
def get_page_data():
    dogs = Dog.query.filter(Dog.id.__gt__(1))
    #当前页码
    current_page = int(request.args.get("page",1))
    #每页的数据条数
    per_page = int(request.args.get("per",20))
    #获得分页对象  paginate(当前页码，数据的个数)
    paginates = dogs.paginate(current_page,per_page)

    # items可以拿到当前页的所有数据
    return render_template("datas.html",dogs = paginates.items)

    # dogs_data = [i.to_dict() for i in paginates.items]
    # data = {
    #     "code":1,
    #     "msg":"ok",
    #     "data": {
    #         "dogs":dogs_data,
    #         #分页器的总页数
    #         "pages":paginates.pages,
    #         #前一页页码
    #         "prev_num":paginates.prev_num,
    #         #判断是否还有前一页
    #         "has_prev":paginates.has_prev,
    #         #判断时候还有后一页
    #         "has_next":paginates.has_next,
    #         #后一页的页码
    #         "next_num":paginates.next_num,
    #         #当前的页码
    #         "current_page":paginates.page
    #     }
    # }

    # return jsonify(data)




@blue.route("/query")
def my_query():
    #or_(条件1，条件2.....)
    dogs = Dog.query.filter(or_(Dog.name.contains("9"),Dog.name.contains("1")))
    return render_template("datas.html",dogs= dogs)


@blue.route("/get_grade/<int:sid>")
def get_grade(sid):
    #先查学生
    stu = Stu.query.get(sid)
    #根据学生的grader_id获取班级信息
    grade = Grade.query.get(stu.grader_id)

    return grade.name


@blue.route("/get_stu/<int:gid>")
def get_stu(gid):
    stu = Stu.query.filter(Stu.grader_id == gid)
    for i in stu:
        print(i)

    return "ok"


@blue.route("/create_my_data/")
def create_my_data():
    tag1 = Tag(title="python")
    tag2 = Tag(title="java")

    db.session.add_all([tag1,tag2])
    db.session.commit()

    book1 = Book(name="笨办法")
    book2 = Book(name="数据分析")

    book1.tags.append(tag1)
    book1.tags.append(tag2)

    book2.tags = [tag1,tag2]
    db.session.add_all([book1,book2])
    db.session.commit()

    return "ok"

#根据标签查找数
@blue.route("/get_book_by_tag/<int:t_id>")
def get_book_by_tag(t_id):
    #查找tag
    tag = Tag.query.get(t_id)
    #通过反向关系来查
    books = tag.books
    for i in books:
        print(i)

    return "ok"


#根据书的id查找标签
@blue.route("/get_tag_by_book/<int:b_id>")
def get_tag_by_book(b_id):
    #获取书
    books = Book.query.get(b_id)
    #获取标签
    tags = books.tags
    for i in tags:
        print(i.title)

    return "ok"