import pandas as pd
import time
import recomend_hotel

### 모델 정확도 테스트용 코드

### 생성된 모델 결과 확인
## id로 된 리뷰 확인
def show_recomended_hotel(hotel_info_df, hotel_review_df, return_data):
    # 확인할 리뷰 리스트
    show_review_list = [1, 5, 10, 20, 40]
    show_review_list = [x-1 for x in show_review_list]

    for i in show_review_list:
        
        hotel_id = return_data[i]['hotel_id']
        review_id_list = return_data[i]['review_id']
        hotel_name = hotel_info_df.loc[int(hotel_id)-1,'hotel_name']
 
        print(f'{i+1} : {hotel_name}------------------')
        for review_id in review_id_list:
            review = hotel_review_df.loc[int(review_id)-1,'contents']
            print(review)
        print('')


if __name__ == '__main__':
    # 데이터 로드
    hotel_info_df = pd.read_csv('./dataset/final/final_hotel_info.csv', encoding='utf-8')
    hotel_review_df = pd.read_csv('./dataset/final/final_hotel_review.csv', encoding='utf-8')
    hotel_review_df.rename(columns={'review' :'contents'}, inplace=True)
    #hotel_review_df = hotel_review_df.loc[hotel_review_df['date'] >= '2020-01']

    region = ['서울', '강원', '여수']
    user_input = '바다뷰가 좋고 직원이 친절했어요'

    start = time.time()
    return_data = recomend_hotel.get_recomended_hotel(region, user_input)
    delta_t = time.time() - start

    show_recomended_hotel(hotel_info_df, hotel_review_df, return_data)
    print(return_data)
    print(delta_t)
