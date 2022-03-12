from flask import Flask,request,jsonify
from flask_restx import Resource, Namespace
from itsdangerous import json
from app import db
from app.dto.userDto import UserDto
from app.models.model import User

user_api = UserDto.api

userParser = user_api.parser()
userParser.add_argument(
    'id', type=str, help='id', location='json', required=True)
userParser.add_argument(
    'name', type=str, help='이름 (예)김길동', location='json', required=True)
userParser.add_argument(
    'email', type=str, help='이메일 (예)example@gmail.com',  location='json',required=True)
@user_api.route("/info", methods=["POST"])
@user_api.doc(parser=userParser)
@user_api.response(200, "성공적으로 수행 됨")
@user_api.response(400, "요청 정보 정확하지 않음")
@user_api.response(500, "API 서버에 문제가 발생하였음")
class UserApi(Resource):
    @user_api.marshal_with(UserDto.user_model, envelope="data")
    @user_api.expect(userParser)
    def post(self):
        args = userParser.parse_args()
        id = args['id']
        name = args['name']
        email = args['email']
        result = User.query\
                .filter(User.user_id == id)\
                .first()
        if result == None:
            user = User(user_id=id,name=name,email=email) 
            db.session.add(user)
            db.session.commit() 
        
        user_result =  User.query\
                .filter(User.user_id == id)\
                .first()

        return user_result