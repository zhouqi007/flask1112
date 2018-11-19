from flask import request
from flask_restful import Resource,marshal,marshal_with

from myapp.args_apis_v1 import *
from myapp.field_apis_v1 import *
from myapp.models import News
from myapp.sql_util import SQLTool


class NewsOneApi(Resource):

    @marshal_with(one_fields)   #我们准备输出的字段名的变量名
    def get(self,*args,**kwargs):
        id = int(request.args.get("id"))
        news = News.query.get_or_404(id)

        return news

#字典套列表
class TwoApi(Resource):

    @marshal_with(two_fields)
    def get(self):
        hobby = ["抽烟","喝酒","推车"]
        return {"hobby":hobby}



class ThreeApi(Resource):
    @marshal_with(three_fields)
    def get(self,**kwargs):
        id = kwargs.get("id")
        print(id,type(id))
        #查数据
        news = News.query.get_or_404(id)
        return {"data":news}



class FourApi(Resource):
    @marshal_with(four_fields)
    def get(self,page,per_page):
        datas = News.query.paginate(page,per_page,error_out=False)

        return {"code":2,"data":datas.items}


#参数的获取，可以根据请求的方式不同获取对应的参数
class FiveApi(Resource):
    def post(self):
        my_args = my_params.parse_args()
        print(my_args)
        print(my_args.hobby)
        return {"msg":"ok"}
    def get(self):
        my_args = my_params.parse_args()
        print(my_args)
        print(my_args.hobby)
        return {"msg":"ok"}


class TestAPI(Resource):

    def get(self):

        tool = SQLTool("root","123","127.0.0.1",3306,"flday05")
        sql = "select * from news"
        res = tool.query(sql)
        print(res)
        return {"ok":"hehe"}



