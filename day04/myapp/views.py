from flask import Blueprint, render_template, request, jsonify, g

from myapp.ext import db
from myapp.models import News
from myapp.ext import cache

blue = Blueprint("day04",__name__)

def init_blue(app):
    app.register_blueprint(blue)


@blue.route("/create_data")
def create_data():
    datas = []
    for i in range(101):
        tem = News(
            title="震惊大新闻"+str(i+1),
            content="娱乐圈潜规则再度升级，这是今年发生的第" + str(i+1) +"起事件"
        )
        datas.append(tem)
    db.session.add_all(datas)
    db.session.commit()

    return "ok"


@blue.route("/index")
@cache.cached(timeout=20)
def index():
    #解析参数
    print("进入函数")
    print("-------",g.tang)
    params = request.args
    page = int(params.get("page"))
    per_page = int(params.get("per_page"))
    paginates = News.query.paginate(page,per_page,error_out=False)   #用all()会报错


    return render_template("index.html",news=paginates.items,pagination=paginates)


@blue.route("/cache")
def  my_cache():
    #先获取ip,拼接key
    ip = request.remote_addr
    key = ip +  "day04"
    #去缓存尝试拿数据
    data = cache.get(key)
    if data:
        print("有数据")
        return jsonify(data)
    else:
        #查数据库
        print("查数据")
        new_data = {
            "code":1,
            "msg":"ok",
            "data":"呵呵哒"
        }
        #设置缓存
        cache.set(key,new_data,30)
        return jsonify(new_data)


@blue.before_request
def heheda():
    #反爬虫 首先检查有没有user_agent,再看IP如果在30秒访问10次，又就杀死
    user_agent = request.user_agent
    g.tang = "咸"
    if not user_agent:
        return jsonify({"code":1000,"msg":"换一个网站"}),500
    ip = request.remote_addr
    key = ip + "fangpa"
    times = cache.get("key")
    if not times:
        cache.set(key,1,30)
    else:
        if int(times) >=3:
            return "搞你妈",404
        else:
            cache.set(key,times+1,30)