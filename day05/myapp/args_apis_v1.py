


#这个会对参数预校验
from flask_restful import reqparse

my_params = reqparse.RequestParser()
#指定解析的位置是get
my_params.add_argument("name",dest="my_name",location="form")  #dest改名
#指定解析的位置是post   required为必填字段
my_params.add_argument("id",type=int,required=True,help="id是必填字段，int类型",location="form")
#指定解析的位置是get和post
my_params.add_argument("hobby",required=True,action="append",location=["form","args"])  #允许一个参数解析多个值，以列表的形式



