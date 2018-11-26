

BROKER_URL = "redis://127.0.0.1:6379/1"  #消息队列
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/2"  #结果存放位置
CELERY_CONCURRENCY = 2 #设置worker数量

TIME_ZONE = "Asia/Shanghai"