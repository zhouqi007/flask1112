#导包
# from flask import Flask, render_template
from flask_script import Manager

# #实例化Flask
# app = Flask(__name__)
from app import create_app

app = create_app()
#实例化manager
manager = Manager(app=app)
#
# #注册路由
# @app.route('/')
# #处理函数
# def hello_world():
#     return 'Hello World!'
#
#
#
# @app.route("/index")
# def index():
#     return render_template("one.html")




#主函数
if __name__ == '__main__':
    #启动flask服务
    # app.run(
    #     host="0.0.0.0",
    #     port=1235,
    #     debug=True
    # )


    manager.run()