from flask_restx import Namespace, fields


class UserDto:
    api = Namespace("user_info", description="사용자 정보 api입니다.")
    user_info_model = api.model(
        "user_info_model",
        {
            "user_id": fields.Integer(readonly=True, description='사용자 id'),
            "name": fields.String(readonly=False, description='사용자 이름'),
            "email": fields.String(readonly=True, description='사용자 지역'),
        },
    )


