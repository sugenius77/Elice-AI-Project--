from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import config
from flask_restx import Api


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False  # 한글깨짐 방지
    app.config.from_object(config)  # config에서 가져온 파일 사용하기
    db.init_app(app)  # SQLAlchemy 객체를 app객체와 이어줌.
    # migrate = Migrate()
    # migrate.init_app(app, db)

    from app.controller.test import test_api, hello_api
    from app.controller.hotelApi import hotel_api
    api = Api(
        app,
        version="0.1.0",
        title="REST API 문서 -호텔 추천 웹 서비스 @2게된다고?",
        description=" 호텔 추천 웹 서비스 REST API(Swagger) 문서입니다.\n \
            소스코드에서 문서를 관리하며,\n \
            문서 상에서 PostMan처럼 직접 API를 작동시키며 테스트 할 수 있습니다.",
        contact="2팀 GitLap : https://kdt-gitlab.elice.io/ai_track/class_03/ai_project/team2/project_nlp",
        license="2팀 license",
        license_url="https://kdt-gitlab.elice.io/ai_track/class_03/ai_project/team2/project_nlp/-/blob/master/README.mdd",
    )
    api.add_namespace(test_api)
    api.add_namespace(hotel_api)

    return app
