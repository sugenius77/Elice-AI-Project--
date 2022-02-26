CREATE TABLE review(
  review_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '리뷰id PK AI',
  contents TEXT COMMENT '리뷰내용',
  hotel_id INTEGER COMMENT '호텔 id',
  review_date DATE COMMENT '리뷰작성 날짜',
  is_positive INTEGER COMMENT '0: 부정, 1: 긍정'
) DEFAULT CHARSET utf8mb4 COMMENT '리뷰 테이블';
CREATE TABLE hotel_info(
  hotel_id int NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '호텔id PK AI',
  hotel_name VARCHAR(255) COMMENT '호텔 이름',
  region VARCHAR(255) COMMENT '호텔 지역',
  hotel_url VARCHAR(2048) COMMENT '호텔 url',
  hotel_img_url VARCHAR(2048) COMMENT '호텔 이미지 url'
) DEFAULT CHARSET UTF8 COMMENT '호텔정보 테이블';

CREATE TABLE user_info(
  user_id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '고객 index PK',
  name text DEFAULT NULL COMMENT '고객 이름',
  email text DEFAULT NULL COMMENT '고객 이메일',
) DEFAULT CHARSET UTF8 COMMENT '고객 정보 테이블';
