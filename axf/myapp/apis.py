
from flask import request, render_template
from flask_mail import Message
from flask_restful import Resource, reqparse, fields, marshal_with

from myapp.ext import mail, cache
from myapp.util import create_uniqu_str
from .models import *



public_fields = {
    "code":fields.Integer(default=1),
    "msg":fields.String(default="ok"),
    "data":fields.String()
}


register_parse = reqparse.RequestParser()
register_parse.add_argument("email",required=True,location="form",help="email必填")
register_parse.add_argument("pwd",required=True,location="form",help="密码必填")
register_parse.add_argument("pwd_confirm",required=True,location="form",help="确认密码必填")


class RegisterAPI(Resource):

    @marshal_with(public_fields)
    def post(self):
        params = register_parse.parse_args()

        email = params.get("email")
        pwd = params.get("pwd")
        pwd_confirm = params.get("pwd_confirm")

        #判断密码和确认密码是否一致
        if pwd != pwd_confirm:
            return {"code":2,"msg":"密码和确认密码不一致"}
        # 创建用户
        res = User.create_user(email=email,pwd=pwd)
        url = "http://" + request.host + "active/" + create_uniqu_str()
        if res:
            # send_email.delay(email, url, res.id,mail, cache)
            msg = Message("欢迎注册爱鲜蜂后台管理",
                          [email],
                          sender="1395947683@qq.com"
                          )
            msg.html = render_template("active.html", url=url)
            mail.send(msg)
            # 拼接
            key = url.split("/")[-1]
            cache.set(key,res.id, timeout=60 * 60)
            return {"data":"/index"}
        else:
            return {"code":3,"msg":"注册失败"}



updates_parse = reqparse.RequestParser()
updates_parse.add_argument("p_id",required=True,location=["args","form"],help="p_id没值")
class UpdateAPI(Resource):

    #修改
    @marshal_with(public_fields)
    def get(self):
        # print("haha")
        p_id = updates_parse.parse_args().get("p_id")
        return {"data":"/item_updates/"+ p_id }


    #删除
    @marshal_with(public_fields)
    def delete(self):
        p_id = updates_parse.parse_args().get("p_id")
        goods = Goods.query.get_or_404(int(p_id))
        db.session.delete(goods)
        db.session.commit()

        return {"data":"delete"}


# 修改订单状态
status_parse = reqparse.RequestParser()
status_parse.add_argument("statu",type=int,required=True,location="form")
status_parse.add_argument("o_id",type=int,required=True,location="form")
class Statu_UpdateAPI(Resource):

    @marshal_with(public_fields)
    def patch(self):
        params = status_parse.parse_args()
        statu = params.get("statu")
        o_id = params.get("o_id")
        status_map = {
            1: "待付款",
            2: "已付款",
            3: "已发货",
            4: "已收货",
            5: "待评价",
            6: "已评价"
        }
        # 修改订单表中的订单状态
        order = Order.query.get_or_404(o_id)
        order.status = statu
        db.session.add(order)
        db.session.commit()
        return {"data":status_map[statu]}
