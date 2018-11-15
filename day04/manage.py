from flask_migrate import MigrateCommand
from flask_script import Manager

from myapp import create_app

app = create_app("debug")
manager = Manager(app=app)
manager.add_command("db",MigrateCommand)


if __name__ == '__main__':
    manager.run()
