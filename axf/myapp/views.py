from flask import Blueprint, render_template, request

from myapp.ext import cache
from myapp.util import get_no_sale, get_data
from .models import *

blue = Blueprint("axf",__name__)

def init_blue(app):
    app.register_blueprint(blue)


#写一些视图函数

#商品管理
@blue.route("/item_view")
def item_view():
    #当前页码
    current_page = int(request.args.get("page",1))
    #每页条数
    per_page = int(request.args.get("per",10))
    #实例化分页器
    paginates = Goods.query.paginate(current_page,per_page,error_out=False)
    return render_template("item/item.html",goods=paginates.items,pagination=paginates,show=True)

#商品搜索
@blue.route("/item_search")
def item_search():
    good_name = request.args.get("good_name")
    goods = Goods.query.filter(Goods.productlongname.contains(good_name))
    if goods:
        # 当前页码
        current_page = int(request.args.get("page", 1))
        # 每页条数
        per_page = int(request.args.get("per", 10))
        # 实例化分页器
        paginates = goods.paginate(current_page, per_page, error_out=False)
        return render_template("item/item.html", goods=paginates.items, pagination=paginates,show=False,good_name=good_name)
    else:
        return "暂无数据"


#商品修改表
@blue.route("/item_updates/<string:p_id>")
def item_update(p_id):
    good = Goods.query.filter(Goods.productid == p_id).first()
    return render_template("item/updates.html",good=good)

#修改
@blue.route("/good_updates/<string:p_id>")
def good_updates(p_id):
    #解析
    params = request.args
    product_id = params.get("product_id")
    product_img = params.get("product_img")
    product_longname = params.get("product_longname")
    product_price = params.get("product_price")
    product_storenums = params.get("product_storenums")
    good = Goods.query.get(int(p_id))
    #修改
    if product_id:
        good.productid = product_id
    if product_img:
        good.productimg = product_img
    if product_longname:
        good.productlongname = product_longname
    if product_price:
        good.price = product_price
    if product_storenums:
        good.storenums = product_storenums
    #保存
    db.session.add(good)
    db.session.commit()

    paginates = Goods.query.paginate(1, 10, error_out=False)
    return render_template("item/item.html", goods=paginates.items, pagination=paginates, show=True)


#订单管理
@blue.route("/order_manage")
def order_manage():
    #查所有的订单
    status_map = {
        1:"待付款",
        2:"已付款",
        3:"已发货",
        4:"已收货",
        5:"待评价",
        6:"已评价"
    }
    all_order = Order.query.all()
    #遍历所有的订单  格式化时间，算钱
    for i in all_order:
        # 格式化时间  添加一个新属性 由于格式化后是字符型，不是时间类型
        i.created_time = i.create_time.strftime("%Y年%m月%d日 %H:%M:%S")
        #算钱 添加一个属性
        i.sum_money = 0
        for j in i.order_items:
            i.sum_money = i.sum_money + j.num * j.buy_money
    #     将订单状态转化为文字  添加新的属性
        i.ch_status = status_map.get(i.status)


    return render_template("order/order_index.html",all_order=all_order,status=status_map)

#不动销
@blue.route("/nosale")
def nosale():
    goods = get_no_sale()
    return render_template("nosale/nosale.html",goods=goods)

@blue.route("/auto_bh")
def auto_bh():
    goods = get_data()
    return render_template("auto/auto.html",goods=goods)


@blue.route("/index")
def index():
    return render_template("index/index.html")


@blue.route("/register")
def register_view():
    return render_template("register/register.html")

@blue.route("/active")
def active(key):
    u_id = cache.get(key)
    if u_id:
        user = User.query.filter(id==int(u_id))
        user.is_active = True
        user.save()
        return "已激活"






