from ..api_1_0 import api_1_0
from flask_restful import Api, Resource
from flask import jsonify

api_user = Api(api_1_0)


class TestApi(Resource):
    def get(self):
        return jsonify({'test_api': 'api is ok'})


api_user.add_resource(TestApi, '/test_api', endpoint='test_api')
