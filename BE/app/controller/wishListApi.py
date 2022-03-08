from flask import Flask
from flask_restx import Resource, Namespace
from itsdangerous import json
from app.dto.hotelDto import HotelDto
from app import db
from app.dto.wishListDto import WishListDto
from app.models.model import WishList, Hotel

wish_list_api = WishListDto.api

# 찜 목록 모두 보기
listParser = wish_list_api.parser()

# 찜 목록 추가
addParser = wish_list_api.parser()
addParser.add_argument(
    'user_id', type=str, location='json', required=True)
addParser.add_argument(
    'hotel_id', type=int, location='json', required=True)

# 찜 목록 제거
subParser = wish_list_api.parser()

@wish_list_api.route("/<string:user_id>", methods=["GET"])
@wish_list_api.doc(parser=listParser)
@wish_list_api.response(200, "성공적으로 수행 됨")
@wish_list_api.response(400, "요청 정보 정확하지 않음")
@wish_list_api.response(500, "API 서버에 문제가 발생하였음")
class ListApi(Resource):
    @wish_list_api.marshal_with(HotelDto.hotel_model, envelope="data")
    @wish_list_api.expect(listParser)
    def get(self,user_id):
        '''찜 목록 보기
        '''
        list = WishList.query\
                .filter(WishList.user_id == user_id)\
                .with_entities(
                    WishList.hotel_id
                )\
                .all()                   

        hotel_list = []

        for i in range(0,len(list)):
            for j in Hotel.query.filter(Hotel.hotel_id == list[i][0]).all(): 
                hotel_list.append(j.__dict__)
        
        return hotel_list



@wish_list_api.route("/add", methods=["POST"])
@wish_list_api.doc(parser=addParser)
@wish_list_api.response(200, "성공적으로 수행 됨")
@wish_list_api.response(400, "요청 정보 정확하지 않음")
@wish_list_api.response(500, "API 서버에 문제가 발생하였음")
class AddApi(Resource):
    @wish_list_api.marshal_with(WishListDto.wish_list_model, envelope="data")
    @wish_list_api.expect(addParser)
    def post(self):
        '''찜 목록 추가
        '''
        args = addParser.parse_args()
        user_id = args['user_id']
        hotel_id = args['hotel_id']
        result = WishList.query\
                .filter(WishList.user_id == user_id, WishList.hotel_id == hotel_id)\
                .first()
        if result == None:
            add_list = WishList(id = None,user_id = user_id, hotel_id = hotel_id)
            db.session.add(add_list)
            db.session.commit( ) 
            
        add_result = WishList.query\
                .filter(WishList.user_id == user_id, WishList.hotel_id == hotel_id)\
                .first()
                
        return add_result
        
        
@wish_list_api.route("/<string:user_id>/<int:hotel_id>", methods=["DELETE"])
@wish_list_api.doc(parser=subParser)
@wish_list_api.response(200, "성공적으로 수행 됨")
@wish_list_api.response(400, "요청 정보 정확하지 않음")
@wish_list_api.response(500, "API 서버에 문제가 발생하였음")
class SubApi(Resource):
    @wish_list_api.marshal_with(WishListDto.wish_list_model, envelope="data")
    @wish_list_api.expect(subParser)
    def delete(self,user_id,hotel_id):
        '''찜 목록 제거
        '''
        result = WishList.query\
                .filter(WishList.user_id == user_id,WishList.hotel_id == hotel_id)\
                .first()
        db.session.delete(result)
        db.session.commit() 
        return result