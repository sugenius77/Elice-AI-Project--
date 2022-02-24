LOAD DATA INFILE 'hotel_info.csv' INTO TABLE hotel_info FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n'(
  region,
  hotel_id,
  hotel_name,
  hotel_url,
  hotel_img_url
);