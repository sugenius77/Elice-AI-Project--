
from flask_restx import Namespace, fields


class HotelDto:
    api = Namespace("hotel", description="호텔관련 api입니다.")
    hotel_info_model = api.model(
        "hotel_info_model",
        {
            "hotel_id": fields.Integer(readonly=True, description='호텔 id'),
            "hotel_name": fields.String(readonly=False, description='호텔 이름'),
            "region": fields.String(readonly=True, description='호텔 지역'),
            "hotel_url": fields.String(readonly=True, description='호텔 url'),
            "hotel_img_url": fields.String(readonly=True, description='호텔 이미지 url')
        },
    )

    review_model = api.model(
        "review_model",
        {
            "review_id": fields.Integer(readonly=True, description='리뷰id'),
            "contents": fields.String(readonly=True, description='리뷰내용'),
            "hotel_id": fields.Integer(readonly=True, description='호텔id'),
            "review_date": fields.Date(readonly=True, description='리뷰작성날짜'),
            "is_positive": fields.Integer(readonly=True, description='긍부정')

        },
    )

    recoHotel_list_model = api.model('recoHotel_list_model', {
        "hotel_id": fields.Integer(readonly=True, description='호텔 id'),
        "hotel_name": fields.String(readonly=False, description='호텔 이름'),
        "region": fields.String(readonly=True, description='호텔 지역'),
        "hotel_url": fields.String(readonly=True, description='호텔 url'),
        "hotel_img_url": fields.String(readonly=True, description='호텔 이미지 url'),
        'reviews': fields.List(fields.Nested(review_model))
    })
