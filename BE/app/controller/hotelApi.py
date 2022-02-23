from flask import Flask
from flask_restx import Resource, Namespace, abort
from app.dto.hotelDto import HotelDto
from app import db
from app.models.model import HotelInfo

hotel_api = HotelDto.api


hotelParser = hotel_api.parser()
hotelParser.add_argument(
    'region', type=str, help='지역 (예)제주', location='args', required=True)
hotelParser.add_argument(
    'search', type=str, help='검색텍스트 (예)바다가 보이고 침대가 편안한 호텔 찾아줘', location='args', required=True)


@hotel_api.route("/recommendHotelList", methods=["GET"])
@hotel_api.doc(parser=hotelParser)
@hotel_api.response(200, "성공적으로 수행 됨")
@hotel_api.response(400, "요청 정보 정확하지 않음")
@hotel_api.response(500, "API 서버에 문제가 발생하였음")
class HelloApi(Resource):
    @hotel_api.marshal_with(HotelDto.hotel_info_model, envelope="data")
    @hotel_api.expect(hotelParser)
    def get(self):
        '''호텔 추천 데이터 
        '''
        args = hotelParser.parse_args()
        region = args['region']
        search = args['search']
        if region == None or search == None:
            abort(400, msg='요청 정보 정확하지 않음.')

        print(
            f'region={region}, search={search}')

        hotel_list = db.session.query(HotelInfo).all()

        return hotel_list
