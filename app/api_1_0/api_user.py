from app import db
from ..api_1_0 import api_1_0
from flask_restful import Api, Resource
from flask import jsonify, request
from app.models.user import User

api_user = Api(api_1_0)


class TestApi(Resource):
    def get(self):
        return jsonify({'test_api': 'api is ok'})


class TestUserApi(Resource):
    def post(self):
        user_info = request.get_json()
        try:
            db.session.add(User(username=user_info['username'], role_id=user_info['role_id']))
            db.session.commit()
        except:
            print("User add error")
            db.session.rollback()
            return False
        else:
            print("User add {}".format(user_info['username']))
            return True
        finally:
            db.session.close()

    def get(self):
        un = request.args.get('username')
        try:
            u_json = User.query.filter_by(username=un).first().to_json()
            print("User get {} ok".format(un))
            return u_json
        except:
            print("User get {} error".format(un))
            return False
        finally:
            db.session.close()


api_user.add_resource(TestApi, '/test_api', endpoint='test_api')
api_user.add_resource(TestUserApi, '/user', endpoint='user')
