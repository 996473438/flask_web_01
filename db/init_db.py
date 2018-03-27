from app import create_app, db


def init_db(database='default'):
    from app.models.user import User
    from app.models.role import Role
    app = create_app(database)
    app.app_context().push()
    db.drop_all()
    db.create_all()


init_db(database='default')
