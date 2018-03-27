from app import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    # lazy='dynamic' 是禁止自动执行查询
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return "<Role {}>".format(self.name)




        # add_role(role_name='admin3')
        # role4 = Role(name='admin4')
        # print(role4)
        # db.session.add(role4)
        # db.session.commit()
