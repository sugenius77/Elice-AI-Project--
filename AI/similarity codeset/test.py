import pandas as pd
import time
#import recomend_hotel
import save_model
import recomend_hotel
from multiprocessing import Pool

### 모델 정확도 테스트용 코드

### 모델 생성
## 0. 테스트용 데이터 설정
def set_test_data(hotel_info_df, hotel_review_df, test_num):
    ## base 변수 설정
    model_name = 'base_d2v_model'
    pos = ["Adjective", "Adverb", "Noun", "Verb"]
    token_min, token_max = 5, 50
    window = 3
    min_count = 10000
    epochs = 30
    
    test_date = set_date(hotel_review_df)
    test_pos = set_pos()

    return_input = []
    
    # 0 : base 그대로 반환
    if test_num == 0:
        return_input.append([hotel_info_df, hotel_review_df, model_name, 
            pos, token_min, token_max, window, min_count, epochs])

    # 1 : 리뷰 시작일별 테스트
    elif test_num == 1:
        test_date = set_date(hotel_review_df)
        
        for index, date in enumerate(test_date):
            hotel_review_df = date
            return_input.append([hotel_info_df, hotel_review_df, f'{test_num}_{index}_d2v', 
            pos, token_min, token_max, window, min_count, epochs])

    # 2 : 품사별 테스트
    elif test_num == 2:
        test_pos = set_pos()

        for index, pos in enumerate(test_pos):
            return_input.append([hotel_info_df, hotel_review_df, f'{test_num}_{index}_d2v', 
            pos, token_min, token_max, window, min_count, epochs])

    # 3 : 토큰 길이별 테스트
    elif test_num == 3:
        test_token = set_token_size()

        for index, token in enumerate(test_token):
            return_input.append([hotel_info_df, hotel_review_df, f'{test_num}_{index}_d2v', 
            pos, token[0], token[1], window, min_count, epochs])

    # 4 : 토큰 길이별 테스트
    elif test_num == 4:
        test_window = set_window_size()

        for index, window in enumerate(test_window):
            return_input.append([hotel_info_df, hotel_review_df, f'{test_num}_{index}_d2v', 
            pos, token_min, token_max, window, min_count, epochs])

    # 5 : min_count 테스트
    elif test_num == 5:
        min_count_list = set_min_count()

        for index, min_count in enumerate(min_count_list):
            return_input.append([hotel_info_df, hotel_review_df, f'{test_num}_{index}_d2v', 
            pos, token_min, token_max, window, min_count, epochs])
    
    # 6 : epochs 테스트
    elif test_num == 6:
        epochs_list = set_epochs()

        for index, epochs in enumerate(epochs_list):
            return_input.append([hotel_info_df, hotel_review_df, f'{test_num}_{index}_d2v', 
            pos, token_min, token_max, window, min_count, epochs])
    
    # 7 : custom
    elif test_num == 7:
        pos = ["Adjective", "Noun", "Verb"]

        return_input.append([hotel_info_df, hotel_review_df, f'base_d2v', 
        pos, token_min, token_max, window, 8000, 40])
    
    return return_input


## 1. 리뷰 기간 : 1년, 6개월
# ['2021-01', '2021-09']
def set_date(hotel_review_df):
    start_date = ['2021-01', '2021-09']
    test_date_list = []

    for date in start_date:
        filtered_date = hotel_review_df[hotel_review_df['date'] >= date]
        test_date_list.append(filtered_date)

    return test_date_list

## 2. 품사별 테스트 : 형용사, 부사, 명사, 동사
# ["Adjective", "Adverb", "Noun", "Verb"], ["Adjective", "Noun", "Verb"], ["Adjective", "Noun"], ["Noun"]
def set_pos():
    pos_list = [["Adjective", "Noun", "Verb"], ["Adjective", "Noun"], ["Noun"]]

    return pos_list

## 3. 토큰 길이별 테스트 : 5<=x<=20, 10<=x<=50, 20<=x<=50
def set_token_size():
    token_size_list = [[5, 20], [10, 50], [20, 50]]

    return token_size_list

## 4. window 사이즈 테스트 : 1, 5
def set_window_size():
    window_size_list = [1, 5]

    return window_size_list

## 5. min_count 테스트 : min_count=len(tagged_corpus_list) // min_count) (1000, 5000, 50000)
def set_min_count():
    min_count = [1000, 5000, 50000]

    return min_count

## 6. epochs 테스트 : 20, 50, 100
def set_epochs():
    epochs = [20, 50, 100]

    return epochs


### 생성된 모델 결과 확인

## id로 된 리뷰 확인
def show_recomended_hotel(hotel_info_df, hotel_review_df, return_data):
    # 확인할 리뷰 리스트
    show_review_list = [1, 5, 10, 20, 40]
    show_review_list = [x-1 for x in show_review_list]

    for i in show_review_list:
        region = return_data[i]['region']
        hotel_id = return_data[i]['hotel_id']
        review_id_list = return_data[i]['review_id']
        hotel_name = hotel_info_df.loc[int(hotel_id)-1,'hotel_name']
 
        print(f'{i+1} : {region} : {hotel_name}------------------')
        for review_id in review_id_list:
            review = hotel_review_df.loc[int(review_id)-1,'contents']
            print(review)
        print('')


if __name__ == '__main__':
    # 데이터 로드
    hotel_info_df = pd.read_csv('./dataset/final/hotel_info.csv', encoding='utf-8')
    hotel_review_df = pd.read_csv('./dataset/final/hotel_review.csv', encoding='utf-8')
    hotel_review_df.rename(columns={'review' :'contents'}, inplace=True)
    hotel_review_df = hotel_review_df.loc[hotel_review_df['date'] >= '2020-01']

    select_num = input("1 : 모델 생성 테스트, 2 : 모델 확인\n")
    ## 모델 생성 -----
    # 테스트 할 변수 선택 : 1(리뷰 시작일), 2(품사), 3(토큰 길이), 4(window), 5(min_count), 6(epochs), 7(custom)
    if select_num == '1':
        test_num = 7
        data = set_test_data(hotel_info_df, hotel_review_df, test_num)

        with Pool(4) as p:
            ret = p.starmap_async(save_model.save_model, data)
            print(ret.get())

    ## 모델 확인 -----
    # 테스트 할 지역, 예시 리뷰 입력
    if select_num == '2':
        region = ['서울', '부산', '강원도', '제주', '여수']
        user_input = '가성비'
        #user_input = '편의점'
        model_name = "base_d2v"

        start = time.time()
        return_data = recomend_hotel.get_recomended_hotel(region, user_input, model_name)
        delta_t = time.time() - start

        show_recomended_hotel(hotel_info_df, hotel_review_df, return_data)
        print(return_data)
        print(delta_t)

