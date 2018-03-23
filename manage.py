from app import create_app, db
from flask_script import Server, Manager, Shell

app = create_app('default')
manager = Manager(app=app)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command('runserver', Server(host='192.168.1.30', port=80, use_debugger=True, use_reloader=True))
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run(default_command='runserver')
    # manager.run(default_command='shell')
