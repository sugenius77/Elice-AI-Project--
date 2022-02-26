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

        # similarity_list = [
        #     {'hotel_id': 1,
        #      'review_id': (1556, 363, 2360, 11605)},
        #     {'hotel_id': 273,
        #      'review_id': (41, 2120, 3711, 222)}
        # ]

        #hotel_info_df = pd.DataFrame(db.session.query(HotelInfo).filter(HotelInfo.region == region), columns=['hotel_id', 'hotel_name', 'region', 'hotel_url', 'hotel_img_url'])
        #hotel_review_df = pd.DataFrame(db.session.query(Review), columns=['review_id', 'contents', 'hotel_id', 'review_date', 'is_positive'])
        hotel_info_df = pd.read_sql(db.session.query(HotelInfo).filter(
            HotelInfo.region == region).statement, db.session.bind)

        hotel_review_df = pd.read_sql(
            db.session.query(Review).join(HotelInfo, Review.hotel_id == HotelInfo.hotel_id).filter(HotelInfo.region == region).statement, db.session.bind)

        similarity_list = recomend_hotel.get_recomended_hotel(
            hotel_info_df, hotel_review_df, search)

        hotels = list(map(hotelval, similarity_list))

        # hotel_list = db.session.query(HotelInfo).all()
        hotel_list = [
            {
                'hotel_id': 1,
                'hotel_name': '테스트 호텔1',
                'region': '제주',
                'hotel_url': 'www.test.com',
                'hotel_img_url': 'https://t-cf.bstatic.com/xdata/images/hotel/square600/331600864.webp?k=3436f6e2fadf753e9d51cdd3554864f07a45bc0702d9c40fc6039b03e8fb12f3&o=&s=1',
                'reviews': [

                    {'review_id': 10,
                     'contents': '바다뷰가 좋아요',
                     'review_date': '2022-02'},
                    {'review_id': 1,
                     'contents': '바다뷰최고 침구 편안',
                     'review_date': '2022-02'},
                    {'review_id': 2,
                     'contents': '바다가 잘보여요',
                     'review_date': '2022-02'},
                    {'review_id': 3,
                     'contents': '직원들이 친절하고 뷰가 너무 좋음',
                     'review_date': '2022-02'}

                ]
            },
            {
                'hotel_id': 2,
                'hotel_name': '테스트 호텔2',
                'region': '제주',
                'hotel_url': 'www.test2.com',
                'hotel_img_url': 'https://t-cf.bstatic.com/xdata/images/hotel/square600/164398650.webp?k=12ca7e07891ffac076fb9e5037c30882b589d0061337494ace1f5dcd351bbfb1&o=&s=1',
                'reviews': [

                    {'review_id': 4,
                     'contents': '바다 전망 최고',
                     'review_date': '2022-02'},
                    {'review_id': 5,
                     'contents': '오션뷰',
                     'review_date': '2022-02'},
                    {'review_id': 6,
                     'contents': '바다 바로 앞',
                     'review_date': '2022-02'}

                ]
            }
        ]

        return hotels


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
