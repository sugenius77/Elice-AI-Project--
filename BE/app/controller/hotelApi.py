from flask import Flask
from flask_restx import Resource, Namespace, abort
from sqlalchemy import func
import pandas as pd

from app.dto.hotelDto import HotelDto
from app import db
from app.models.model import HotelInfo, Review
from app.service import recomend_hotel

hotel_api = HotelDto.api


hotelParser = hotel_api.parser()
hotelParser.add_argument(
    'region', type=str, help='지역 (예)제주|서울', location='args', required=True)
hotelParser.add_argument(
    'search', type=str, help='검색텍스트 (예)바다가 보이고 침대가 편안한 호텔 찾아줘', location='args', required=True)


@hotel_api.route("/recommendHotelList", methods=["GET"])
@hotel_api.doc(parser=hotelParser)
@hotel_api.response(200, "성공적으로 수행 됨")
@hotel_api.response(400, "요청 정보 정확하지 않음")
@hotel_api.response(500, "API 서버에 문제가 발생하였음")
class HelloApi(Resource):
    @hotel_api.marshal_with(HotelDto.recoHotel_list_model, envelope="data")
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

        #hotel_info_df = pd.DataFrame(db.session.query(HotelInfo).filter(HotelInfo.region == region), columns=['hotel_id', 'hotel_name', 'region', 'hotel_url', 'hotel_img_url'])
        #hotel_review_df = pd.DataFrame(db.session.query(Review), columns=['review_id', 'contents', 'hotel_id', 'review_date', 'is_positive'])

        # hotel_info_df = pd.read_sql(db.session.query(HotelInfo).filter(
        #     HotelInfo.region == region).statement, db.session.bind)

        # hotel_review_df = pd.read_sql(
        #     db.session.query(Review).join(HotelInfo, Review.hotel_id == HotelInfo.hotel_id).filter(HotelInfo.region == region).statement, db.session.bind)

        if region == "전체":
            region_list = ['서울', '부산', '제주', '강원', '여수']
        else:
            region_list = region.split("|")

        print(region_list)
        similarity_list = recomend_hotel.get_recomended_hotel(
            region_list, search)

        hotel_list = list(map(hotelval, similarity_list))

        return hotel_list


def hotelval(x):

    hotels = {}
    for u in db.session.query(HotelInfo).filter(HotelInfo.hotel_id == x['hotel_id']).all():
        hotels = u.__dict__

    reviews = list(map(reviewval, x['review_id']))
    hotels['reviews'] = reviews
    res = hotels
    return res


def reviewval(y):

    return db.session.query(Review.review_id, Review.is_positive, Review.hotel_id, Review.contents, func.date_format(Review.review_date, '%Y-%m').label('review_date')).filter(Review.review_id == y).all()
