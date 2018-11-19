from flask import Blueprint, url_for, redirect, render_template, request, make_response, abort, session

blue = Blueprint("hello",__name__)

@blue.route("/myblue")
def hello_blue_print():
    return "我是蓝图规划URL"

#add_url_rule(路由名，蓝图名，函数名)
# blue.add_url_rule("/myblue","hello",hello_blue_print)

#可以指定传入数据的类型，但是输出一定要是字符串型
@blue.route("/param/<int:id>")
def param(id):
    print(id)
    print(type(id))
    return str(id)

#接受路径
@blue.route("/param/<path:my_path>")
def param_path(my_path):
    print(my_path)
    print(type(my_path))
    import uuid
    uuid_val = uuid.uuid4()
    return str(uuid_val)


#只接受uuid字符串码
@blue.route("/param/<uuid:my_uuid>")
def param_uuid(my_uuid):
    print(my_uuid)
    return "ok"

#使用any后参数只可以使用any规定的值  methods为请求的方式
@blue.route("/my_any/<any(a,b,c):p>" ,methods = ["GET","POST"])
def my_any(p):
    # print(p)

    #获取无参数的反向解析路径 url_for(蓝图名.函数名)
    # res = url_for("hello.hello_blue_print")

    #获取带参数的函数的路径  url_for(蓝图名.函数名,参数名1=参数值1...)  若不存在的参数不存在的用默认用？连接，多个用&连接
    res = url_for("hello.param",id=1)

    #重定向 redirect
    return redirect(res)

#页面的添加使用
@blue.route("/index")
def index():
    return render_template("one.html")


#请求 request
@blue.route("/req",methods=["GET","POST","PUT","DELETE"])
def look_req():
    req = request
    print(req)
    print("method",req.method)
    #path为端口后面的路径
    print("path",req.path)
    #获取get请求的参数用args   args时一个列表中加元祖[(key,value)]  key可以重复，用get(key)获取一个，getlist(key)获取多个
    print("args",req.args)
    print("args1",req.args.get("name"))
    #url为完整的路径
    print("url",req.url)
    #获取post请求参数
    print("form",req.form)
    print("base_url", req.base_url)
    #文件上传
    print("file",req.files)
    # print(dir(req))

    #请求客户端地址
    print("ip",req.remote_addr)
    return "ok"


#响应 make_response(响应内容，响应状态码)
@blue.route("/response")
def my_response():
    response = make_response("hehe")
    #主动终止，括号里面时状态码
    abort(403)
    return response

#捕获异常
@blue.errorhandler(403)
def handle_403(e):
    print(e)
    return "无权限"


@blue.route("/home")
def home():
    #用session获取缓存
    uname = session.get("uname")
    #通过cookies获取
    # uname = request.cookies.get("name")
    uname = uname if uname else "游客"
    return render_template("home.html",uname=uname )


@blue.route("/login",methods = ["GET","POST"])
def login():
    #根据请求方式获取页面
    if request.method == "GET":
        return render_template("login.html")
    #post请求提交用户信息
    elif request.method == "POST":
        name = request.form.get("name")

        #用session设置缓存
        session["uname"] = name
        #重定向，页面跳转
        response = redirect(url_for("hello.home"))
        #cooki设置缓存
        # response.set_cookie("name",name,30)

        return response

    else:
        abort(405)

@blue.route("/logout")
def logout():
    #页面的跳转
    response = redirect(url_for("hello.home"))
    # response.delete_cookie("name")
    session.pop("uname")
    return response