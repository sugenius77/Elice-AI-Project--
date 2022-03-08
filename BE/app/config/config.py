from dotenv import load_dotenv
import os

load_dotenv()
# dotenv 사용
print(os.environ['FLASK_ENV'])
if os.environ['FLASK_ENV'] == 'production':
    DB_CONNECT = os.environ['DB_CONNECT']
else:
    DB_CONNECT = os.environ['DB_CONNECT_DEV']
# local .env 파일 사용
print(DB_CONNECT)
SQLALCHEMY_DATABASE_URI = DB_CONNECT
SQLALCHEMY_TRACK_MODIFICATIONS = False
