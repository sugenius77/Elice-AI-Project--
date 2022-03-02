from flask_restx import Namespace, fields

class WishListDto:
    api = Namespace("wish-list", description="찜 기능 api입니다.")
    wish_list_model = api.model(
        "wish_list_model",
        {   
            "id": fields.Integer(readonly=False, description='id'),
            "user_id": fields.String(readonly=False, description='사용자 id'),
            "hotel_id": fields.Integer(readonly=False, description='호텔 id'),
        },
    )

