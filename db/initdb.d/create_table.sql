DROP DATABASE IF EXISTS nlp;
CREATE DATABASE nlp;
USE nlp;
CREATE TABLE review(
  review_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '리뷰id PK AI',
  contents TEXT COMMENT '리뷰내용',
  hotel_id INTEGER COMMENT '호텔 id',
  review_date DATE COMMENT '리뷰작성 날짜',
  is_positive INTEGER COMMENT '0: 부정, 1: 긍정'
) DEFAULT CHARSET utf8mb4 COMMENT '리뷰 테이블';
CREATE TABLE hotel(
  hotel_id int NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '호텔id PK AI',
  hotel_name VARCHAR(255) COMMENT '호텔 이름',
  region VARCHAR(255) COMMENT '호텔 지역',
  hotel_url VARCHAR(2048) COMMENT '호텔 url',
  hotel_img_url VARCHAR(2048) COMMENT '호텔 이미지 url'
) DEFAULT CHARSET UTF8 COMMENT '호텔정보 테이블';
CREATE TABLE `user`(
  `user_id` varchar(255) NOT NULL PRIMARY KEY COMMENT '사용자id PK',
  `name` varchar(255) DEFAULT NULL COMMENT '사용자 이름',
  `email` varchar(255) DEFAULT NULL COMMENT '사용자 이메일'
) DEFAULT CHARSET UTF8 COMMENT '사용자 정보 테이블';
CREATE TABLE `wish_list` (
  `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL COMMENT '사용자id',
  `hotel_id` int(11) NOT NULL COMMENT '호텔id'
) DEFAULT CHARSET UTF8 COMMENT '찜 목록 테이블';