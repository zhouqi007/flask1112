from celery import Celery
from flask import render_template
from flask_mail import Message

import celery_conf


app = Celery(__name__)
#从配置文件拿到celery的配置文件
app.config_from_object(celery_conf)

# @app.tasks
# def send_email(reciver,url,u_id,mail, cache):
#
#     msg = Message("欢迎注册爱鲜蜂后台管理",
#                   [reciver],
#                   sender="1395947683"
#                   )
#     msg.html = render_template("active.html",url=url)
#     mail.send(msg)
#     #拼接
#     key = url.split("/")[-1]
#     cache.set(key,u_id,time_out=60*60)