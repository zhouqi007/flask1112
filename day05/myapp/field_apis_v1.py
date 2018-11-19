from flask_restful import fields

one_fields = {
    "id":fields.Integer,
    "title":fields.String,
    "hehe":fields.String(default="lala")
}

two_fields = {
    "name":fields.String(default="tom"),
    #列表里是字符串
    "hobby":fields.List(fields.String)
}

#字典套字典
three_fields = {
    "code":fields.Integer(default=1),
    "msg":fields.String(default="ok"),
    "data":fields.Nested(one_fields)   #做关联
}


#字典套列表套字典
four_fields = {
    "code":fields.Integer(default=1),
    "msg":fields.String(default="ok"),
    "data":fields.List(fields.Nested(one_fields))
}