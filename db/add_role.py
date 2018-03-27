from app.models.role import Role
from app.models.user import User
from app import db


def add_role(role_name):
    role = Role(name=role_name)
    print(role)
    db.session.add(role)
    db.session.commit()

add_role(role_name='admin3')