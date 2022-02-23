from dotenv import load_dotenv
import os

load_dotenv()
# dotenv 사용 

DB_CONNECT = os.environ['DB_CONNECT']
# local .env 파일 사용

SQLALCHEMY_DATABASE_URI = DB_CONNECT
SQLALCHEMY_TRACK_MODIFICATIONS = False