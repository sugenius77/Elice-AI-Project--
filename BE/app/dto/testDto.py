
from flask_restx import Namespace, fields


class HelloDto:
    api = Namespace("helloTest", description="테스트 api입니다.")
    test_model1 = api.model(
        "test_model1",
        {
            "id": fields.Integer(readonly=True, description='아이디'),
            "review": fields.String(readonly=True, description='지역 (구)'),
            "date": fields.Date
        },
    )

    test_model2 = api.model(
        "test_model2",
        {
            "id": fields.Integer,
            "review": fields.String
        },
    )

    test_model3 = api.model('test_model3', {
        'tests1': fields.List(fields.Nested(test_model1)),
        'tests2': fields.List(fields.Nested(test_model2)),
    })
