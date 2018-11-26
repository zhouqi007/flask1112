from math import ceil

import hashlib
import uuid
from sqlalchemy import create_engine
from datetime import datetime,timedelta

engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/myaxf")


def enc_pwd(pwd):
    sha256 = hashlib.sha256()
    sha256.update(pwd.encode("utf-8"))
    return sha256.hexdigest()

def create_uniqu_str():
    uuid_str = str(uuid.uuid4()).encode("utf-8")
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()

# 将sql查询的数据转换成数据    res.cursor.description 的得到的是结果的集合，第一个为字段名
def data_to_dict(cursor):
    heads = [i[0] for i in cursor.description]
    #cursor.fetchall() 获取所有结果的结合   ((495,), (496,), (497,))
    return [dict(zip(heads,col)) for col in cursor.fetchall()]

#15天销售的商品情况
def get_no_sale():
    #创建对数据库的连接
    con = engine.connect()
    #获取十五天之前的时间  timedelta()指定减得是什么
    fifteen_day = datetime.now() - timedelta(days=15)

    sql = """
        SELECT 
          DISTINCT  i.goods_id
        FROM myaxf_order AS o 
        LEFT  JOIN  myaxf_orderitem AS i
        ON 
          o.id = i.order_id
        WHERE 
          o.create_time > '{my_time}'
        AND 
        o.create_time < now()
    """.format(my_time=str(fifteen_day))

    #执行数据库语句  销售的商品  得到数据库对象
    res = con.execute(sql)
     #结果是列表套字典  [{'goods_id': 495}, {'goods_id': 496}, {'goods_id': 497}]
    goods_ids = data_to_dict(res.cursor)
    # print(goods_ids)

    #拿出商品id变成一个集合
    goods_tep = []
    for i in goods_ids:
        # i.values() 得到的结果是dict_values([495])
        goods_tep.append(list(i.values())[0])


    #所有的商品
    all_goods_sql = """
        SELECT id,storenums,price,productlongname,productid FROM axf_goods;
    """
    # 结果是列表套字典
    all_goods = data_to_dict(con.execute(all_goods_sql).cursor)

    # 拿出商品id变成一个集合
    goods_map = {}
    # 将数据化成以id为key，其余属性组成的字典为value，以便后面查询
    for i in all_goods:
        goods_map[i.get("id")] = {
            "productid":i.get("productid"),
            "storenums":i.get("storenums"),
            "price":i.get("price"),
            "productlongname":i.get("productlongname")
        }

    #转成集合相减 得到不动销产品id
    result = list(set(goods_map.keys())-set(goods_tep))

    #将所有每个不动销商品的属性装在一个字典李，然后将所有字典用列表装
    goods = []
    for j in result:
        goods.append(goods_map[j])
    return goods

def get_data():
    get_goods_day = 3

    my_time = datetime.now() - timedelta(days=get_goods_day*5)
    sql = """
        SELECT
          i.goods_id,sum(i.num) as sum_num ,ag.storenums,ag.productlongname,ag.productid
        FROM
          myaxf_order AS o 
        LEFT JOIN 
          myaxf_orderitem AS i 
        ON 
           o.id = i.order_id
        LEFT JOIN 
          axf_goods AS ag 
        ON 
          i.goods_id = ag.id
        WHERE 
          o.create_time>'{my_time}'
        AND 
          o.create_time<now()
        GROUP BY
          i.goods_id
    """.format(my_time=my_time)

    con = engine.connect()
    res = con.execute(sql)
    result = data_to_dict(res.cursor)
    bh_tmp = {}
    # 求平均销量，然后乘以get_goods_day就得到未来三天需要的商品数量
    for i in result:
        #需要补的货
        i["need"] = ceil(float(i.get("sum_num")) /((get_goods_day)*6) * get_goods_day)
        #如果补货大于库存，就补货
        if i["need"]>i["storenums"]:
            bh_tmp[i['goods_id']] = {
                "bh_num":int(i["need"])- int(i["storenums"]),
                "storenums":i["storenums"],
                "productlongname":i["productlongname"],
                "productid":i["productid"]
            }

    result = list(bh_tmp.values())
    return result