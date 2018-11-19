# from flask import Blueprint, request, jsonify
#
# from myapp.ext import db
# from myapp.urls_apis_v1 import api
# from .models import News
# from flask_restful import Resource
#
# blue = Blueprint("day05", __name__)
#
#
# def init_blue(app):
#     app.register_blueprint(blue)
#
#
# @blue.route("/news", methods=["GET", "POST", "PUT", "DELETE"])
# def news_api():
#     if request.method == "GET":
#         # 获取数据
#         id = int(request.args.get("id", 1))
#         news = News.query.get_or_404(id)
#         res = {
#             "code": 1,
#             "msg": "ok",
#             "data": news.to_dict()
#         }
#         return jsonify(res)
#
#     elif request.method == "POST":
#         # 创建数据
#         params = request.form
#         title = params.get("title")
#         content = params.get("content")
#         n_type = params.get("type")
#
#         news = News(
#             title=title,
#             content=content,
#             type=n_type
#         )
#         db.session.add(news)
#         db.session.commit()
#         res = {
#             "code": 1,
#             "msg": "ok",
#             "data": news.to_dict()
#         }
#         return jsonify(res), 201
#
#     elif request.method == "PUT":
#         # 修改数据
#         params = request.form
#         id = int(params.get("id"))
#         # 知道修改哪一个
#         news = News.query.get_or_404(id)
#         # 能解析到数据，就用解析的，解析不到就用原来的
#         title = params.get("title", news.title)
#         content = params.get("content", news.content)
#         n_type = params.get("type", news.type)
#
#         news.title = title
#         news.content = content
#         news.type = n_type
#
#         db.session.add(news)
#         db.session.commit()
#
#         res = {
#             "code": 1,
#             "msg": "ok",
#             "data": news.to_dict()
#         }
#         #201代表修改或创建成功
#         return jsonify(res), 201
#
#     else:
#         # 删除数据
#         id = int(request.form.get("id"))
#         news = News.query.get_or_404(id)
#
#         res = {
#             "code": 1,
#             "msg": "ok",
#             "data": news.to_dict()
#         }
#         db.session.delete(news)
#         db.session.commit()
#         #204代表删除成功
#         return jsonify(res), 204
#
#
# class NewsAPiTest(Resource):
#
#     def get(self):
#         return {"data":"heheda"}
#
# #可以写多个url查询
# api.add_resource(NewsAPiTest,"/test","/heheda")