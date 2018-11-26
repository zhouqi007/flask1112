import datetime

from myapp.ext import db
from myapp.util import enc_pwd


class User(db.Model):
    id=db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(30),
        nullable=True
    )
    email = db.Column(
        db.String(30),
        unique=True,
        index=True
    )
    pwd = db.Column(
        db.String(255),
        nullable=False
    )
    is_active = db.Column(
        db.Boolean,
        default=False,
    )
    is_delete = db.Column(
        db.Boolean,
        default=False,
    )


    #创建用户方法
    @classmethod
    def create_user(cls,email,pwd,name=None):
#         email 能不能搜到一个用户,检查email
        users = User.query.filter(User.email==email)
        if users.count() > 0:
            return None
#        加密pwd
        user_pwd = enc_pwd(pwd)
#         创建用户
        name = name if name else email
        user = cls(
            name=name,
            email=email,
            pwd = user_pwd
        )
        db.session.add(user)
        db.session.commit()
        return user

    #重置密码
    def set_pwd(self,pwd):
        if not pwd and len(pwd)==0:
            raise Exception("密码不能为空")
        #对密码加密
        self.pwd = enc_pwd(pwd)
        db.session.add(self)
        db.session.commit()

        return True

    #检测密码
    def check_pwd(self,pwd):
        u_pwd = enc_pwd(pwd)

        if u_pwd == self.pwd:
            return True
        else:
            return False

class Goods(db.Model):
    __tablename__ = "axf_goods"  #修改表名

    id =db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    productid = db.Column(
        db.String(20)
    )
    productimg = db.Column(
        db.String(255)
    )
    productname = db.Column(
        db.String(130),
    )
    productlongname = db.Column(
        db.String(190)
    )
    isxf = db.Column(
        db.Boolean,
        default=False
    )
    pmdesc = db.Column(
        db.Integer
    )
    specifics = db.Column(
        db.String(40)
    )
    price = db.Column(
        db.Numeric(precision=10,scale=2)  #最大长度10位，小数点两位
    )
    marketprice = db.Column(
        db.Numeric(precision=10, scale=2)
    )
    categoryid = db.Column(
        db.Integer
    )
    childcid = db.Column(
        db.Integer
    )
    childcidname = db.Column(
        db.String(30)
    )
    dealerid = db.Column(
        db.String(30)
    )
    storenums = db.Column(
        db.Integer
    )
    productnum = db.Column(
        db.Integer
    )
    order_items_goods = db.relationship(
        "OrderItem",
        backref ="goods",
        lazy=True
    )

#订单
class Order(db.Model):
    __tablename__ = "myaxf_order"  # 修改表名

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    user_id = db.Column(
        db.Integer,
        # db.ForeignKey("myaxf_myuser.id")
    )

    create_time = db.Column(
        db.DateTime,
        default=datetime.datetime.now()
    )
    status = db.Column(
        db.Integer
    )
    order_items = db.relationship(
        "OrderItem",
        backref="order",
        lazy=True
    )

#订单详情
class OrderItem(db.Model):
    __tablename__ = "myaxf_orderitem"  # 修改表名

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    order_id = db.Column(
        db.Integer,
        db.ForeignKey("myaxf_order.id")
    )
    goods_id = db.Column(
        db.Integer,
        db.ForeignKey("axf_goods.id")
    )
    num = db.Column(
        db.Integer
    )
    buy_money =db.Column(
        db.Numeric(precision=10,scale=2)
    )
