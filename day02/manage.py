
from flask_script import Manager

from myapp import create_app

#实例化app
app = create_app()

# SESSION_TYPE = "redis"
#实例化manage
manager = Manager(app = app)

if __name__ == '__main__':
    #运行manage
    manager.run()



