from app import db
from datetime import date, datetime


class HotelInfo(db.Model):
    __tablename__ = "hotel_info"
    hotel_id = db.Column(db.Integer, primary_key=True,
                         nullable=False, autoincrement=True)
    hotel_name = db.Column(db.String, nullable=False)
    region = db.Column(db.String, nullable=False)
    hotel_url = db.Column(db.String, nullable=False)
    hotel_img_url = db.Column(db.String, nullable=False)

    def __init__(self, hotel_name, region, hotel_url, hotel_img_url):
        self.hotel_name = hotel_name
        self.region = region
        self.hotel_url = hotel_url
        self.hotel_img_url = hotel_img_url


class Review(db.Model):
    __tablename__ = 'review'
    review_id = db.Column(db.Integer, primary_key=True,
                          nullable=False, autoincrement=True)
    contents = db.Column(db.String, nullable=False)
    hotel_id = db.Column(db.Integer, nullable=False)
    review_date = db.Column(db.Date, nullable=False)
    is_positive = db.Column(db.Integer, nullable=False)

    def __init__(self, contents, hotel_id, is_positive):
        self.contents = contents
        self.hotel_id = hotel_id
        self.is_positive = is_positive

class UserInfo(db.Model):
    __tablename__ = "user_info"
    user_id = db.Column(db.Integer, primary_key=True,
                         nullable=False, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        