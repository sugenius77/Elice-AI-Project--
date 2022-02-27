import pandas as pd

import recomend_hotel


# 테스트용 코드

# csv -> db로 데이터 변경 필요
hotel_info_df = pd.read_csv('./dataset/final/hotel_info.csv', encoding='utf-8')
hotel_review_df = pd.read_csv(
    './dataset/final/hotel_review.csv', encoding='utf-8')

# 프론트에서 받은 값으로 변경 필요
user_input = '직원이 친절하고 화장실이 깨끗'

recomended_hotel_data = recomend_hotel.get_recomended_hotel(
    hotel_info_df, hotel_review_df, user_input)

print(recomended_hotel_data)
