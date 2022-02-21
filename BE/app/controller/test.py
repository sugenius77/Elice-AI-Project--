from flask import Flask
from flask_restx import Resource, Namespace, abort
from app.dto.testDto import HelloDto

test_api = Namespace("test_api", description="flask-restx 참조용 api")
hello_api = HelloDto.api


@test_api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


helloParser = hello_api.parser()
helloParser.add_argument(
    'region', type=str, help='지역 (예)제주', location='args', required=True)
helloParser.add_argument(
    'search', type=str, help='검색텍스트 (예)바다가 보이고 침대가 편안한 호텔 찾아줘', location='args', required=True)


@hello_api.route("/test", methods=["GET"])
@hello_api.doc(parser=helloParser)
@hello_api.response(200, "성공적으로 수행 됨")
@hello_api.response(400, "요청 정보 정확하지 않음")
@hello_api.response(500, "API 서버에 문제가 발생하였음")
class HelloApi(Resource):
    @hello_api.marshal_with(HelloDto.test_model1, envelope="data")
    @hello_api.expect(helloParser)
    def get(self):
        '''호텔 추천 데이터 
        '''
        args = helloParser.parse_args()
        region = args['region']
        search = args['search']
        if region == None or search == None:
            abort(400, msg='요청 정보 정확하지 않음.')

        print(
            f'region={region}, search={search}')
        return {
            "id": 1,
            "review": '바다뷰가 정말 좋아요. 침대도 편안해요.',
            "date": '2021-03-01'
        }
