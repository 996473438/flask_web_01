from . import main
from app.models.role import Role
from app.models.user import User
from app import db


def add_role(role_name):
    role = Role(name=role_name)
    print(role)
    db.session.add(role)
    db.session.commit()


# def add_user(user_name, role_name):
#     r = Role(name=role_name)
#     u = User(username=user_name, role=r)
#     db.session.add(u)
#     return db.session.commit()

def add_user(user_name, role_id):
    u = User(username=user_name, role_id=role_id)
    db.session.add(u)
    return db.session.commit()


@main.route('/', methods=['GET', 'POST'])
def index():
    # add_user('liuxin', 'admin')
    # add_user('menghaimin', 'admin')
    # add_role(role_name='admin99')
    # add_user('liming', 1)
    print(User.query.all())
    print(User.query.filter_by(username='liuxin').first())
    print(Role.query.filter_by(name='admin').first().users.all())
    return "<h1>test</h1>"


@main.route('/test', methods=['GET', 'POST'])
def test():
    return "test, this is my test"
