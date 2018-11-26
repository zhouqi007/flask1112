from os import environ

CACHE = {
    "default":{
        "CACHE_TYPE":"redis",
        "CACHE_REDIS_URL":"redis://127.0.0.1:6379/7"
    },
    "debug":{
        "CACHE_TYPE":"redis",
        "CACHE_REDIS_URL":"redis://127.0.0.1:6379/8"
    }
}

def get_db_uri(conf):
    uri = "{backend}+{engine}://{user}:{pwd}@{host}:{port}/{db}".format(
        backend=conf.get("backend"),
        engine=conf.get("engine"),
        user=conf.get("user"),
        pwd=conf.get("pwd"),
        host=conf.get("host"),
        port=conf.get("port"),
        db=conf.get("db")
    )
    # print(uri)
    return uri

class Config:
    DEBUG = False
    Online = False
    SECRET_KEY = "sdhisauhyryuoj"
    SESSION_TYPE = "redis"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #邮箱配置
    MAIL_SERVER = "smtp.qq.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = "1395947683@qq.com"
    MAIL_PASSWORD = "htogmbimsmodbacj"
    MAIL_DEFAULT_SENDER = MAIL_USERNAME


class DebugConfig(Config):
    DEBUG = True
    DATABASE = {
        "engine":"pymysql",
        "backend":"mysql",
        "host":"127.0.0.1",
        "port":3306,
        "user":environ.get("DB_USER"),
        "pwd":environ.get("DB_PWD"),
        "db":"myaxf"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

conf = {
    "debug": DebugConfig
}

