CREATE TABLE positive_review(
  review_id int NOT NULL PRIMARY KEY COMMENT '리뷰 index PK',
  contents TEXT COMMENT '리뷰내용',
  hotel_id int COMMENT '호텔 id'
) DEFAULT CHARSET UTF8 COMMENT '긍정리뷰 테이블';
CREATE TABLE nagative_review(
  review_id int NOT NULL PRIMARY KEY COMMENT '리뷰 index PK',
  contents TEXT COMMENT '리뷰내용',
  hotel_id int COMMENT '호텔 id'
) DEFAULT CHARSET UTF8 COMMENT '부정리뷰 테이블';