from flask import Flask
from flask_restx import Resource, Namespace


test_api = Namespace("test_api", description="flask-restx 참조용 api")


@test_api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


