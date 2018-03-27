from app.models.user import User
from app.models.role import Role
from app import db


def add_user(username, role_name):
    r = Role(name=role_name)
    u = User(username=username, role=r)
    db.session.add(u)
    return db.session.commit()


print(add_user('liuxin', 'admin'))
