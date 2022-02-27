import pandas as pd
import time
import recomend_hotel
import save_model

## 테스트용 코드

# csv -> db로 데이터 변경 필요
hotel_info_df = pd.read_csv('./dataset/final/hotel_info.csv', encoding='utf-8')
gangwondo_info = hotel_info_df[hotel_info_df['region'] == '강원도']
hotel_review_df = pd.read_csv('./dataset/final/hotel_review.csv', encoding='utf-8')
hotel_review_df.rename(columns={'review' :'contents', 'review_index' : 'review_id', 'hotel_index' :'hotel_id'}, inplace=True)


# 프론트에서 받은 값으로 변경 필요
user_input = '화장실이 깨끗하고 객실이 넓은'

#save_model.save_model(hotel_info_df, hotel_review_df)
start = time.time()
data = recomend_hotel.get_recomended_hotel(['강원도', '서울', '부산'], user_input)
delta_t = time.time() - start
print(data)
print(delta_t)