from flask import Flask,request,jsonify
from flask_restx import Resource, Namespace
from app import db
from ..models.model import UserInfo

user_api = Namespace("user_info")


@user_api.route('/info')
class UserApi(Resource):
    def post(self):
        name = request.form.get('name')
        email = request.form.get('email')
        print(name)
        print(email)
        result = UserInfo.query\
                .filter(UserInfo.name == name, UserInfo.email == email)\
                .first()
                
        if result == None:
            user = UserInfo(user_id=None,name=name,email=email) 
            db.session.add(user)
            db.session.commit()
    
        return jsonify({"status":200,"message":"update success"})

