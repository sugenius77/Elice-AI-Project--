from flask_restx import Namespace, fields

class UserDto:
    api = Namespace("user", description="사용자 정보 api입니다.")
    user_model = api.model(
        "user_model",
        {
            "user_id": fields.String(readonly=True, description='사용자 id'),
            "name": fields.String(readonly=False, description='사용자 이름'),
            "email": fields.String(readonly=True, description='사용자 이메일'),
        },
    )

