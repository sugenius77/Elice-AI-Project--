from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_migrate import Migrate

from app.config import config


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False  # 한글깨짐 방지
    app.config.from_object(config)  # config에서 가져온 파일 사용하기

    app.config.SWAGGER_UI_DOC_EXPANSION = "list"  # 펼쳐짐
    app.config.SWAGGER_UI_OPERATION_ID = True
    app.config.SWAGGER_UI_REQUEST_DURATION = True
    # app.config.SWAGGER_SUPPORTED_SUBMIT_METHODS = ["get"]  # Try it out 제공
    app.config['RESTX_MASK_SWAGGER'] = False
    CORS(app)

    db.init_app(app)  # SQLAlchemy 객체를 app객체와 이어줌.
    # migrate = Migrate()
    # migrate.init_app(app, db)

    from app.controller.test import test_api, hello_api
    from app.controller.hotelApi import hotel_api
    from app.controller.userApi import user_api
    from app.controller.wishListApi import wish_list_api
    
    api = Api(
        app,
        version="0.1.0",
        title="키보드로 소문난 호텔 OpenAPI Specification ",
        description="다른 방문객들의 리뷰로 호텔을 맞춤 추천하는 웹&모바일 서비스의 API DOC",
        contact="2게된다고?팀 GitLap : https://kdt-gitlab.elice.io/ai_track/class_03/ai_project/team2/project_nlp",
        license="2게된다고?팀 license",
        license_url="https://kdt-gitlab.elice.io/ai_track/class_03/ai_project/team2/project_nlp/-/blob/master/README.mdd",
    )
    api.add_namespace(test_api)
    api.add_namespace(hotel_api)
    api.add_namespace(user_api)
    api.add_namespace(wish_list_api)
    return app
