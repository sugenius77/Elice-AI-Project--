from app import db
from datetime import date, datetime


class Hotel(db.Model):
    __tablename__ = "hotel"
    hotel_id = db.Column(db.Integer, primary_key=True,
                         nullable=False, autoincrement=True)
    hotel_name = db.Column(db.String, nullable=False)
    region = db.Column(db.String, nullable=False)
    hotel_url = db.Column(db.String, nullable=False)
    hotel_img_url = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    positive_keywords = db.Column(db.String, nullable=False)
    negative_keywords = db.Column(db.String, nullable=False)

    def __init__(self, hotel_name, region, hotel_url, hotel_img_url, address, positive_keywords, negative_keywords):
        self.hotel_name = hotel_name
        self.region = region
        self.hotel_url = hotel_url
        self.hotel_img_url = hotel_img_url
        self.address = address
        self.positive_keywords = positive_keywords
        self.negative_keywords = negative_keywords


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


class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.String, primary_key=True,
                        nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email


class WishList(db.Model):
    __tablename__ = "wish_list"
    id = db.Column(db.Integer, primary_key=True,
                   nullable=False)
    user_id = db.Column(db.String,
                        nullable=False)
    hotel_id = db.Column(db.Integer,
                         nullable=False)

    def __init__(self, id, user_id, hotel_id):
        self.id = id
        self.user_id = user_id
        self.hotel_id = hotel_id
