import pandas as pd
import numpy as np
import os
import time

from pororo import Pororo
from sklearn.metrics.pairwise import cosine_similarity
from multiprocessing import Pool


def get_similarity(review, vec):
    similarity = review['vector'].apply(lambda x: cosine_similarity(x.reshape(1, -1), vec.reshape(1, -1)))
    return similarity

def get_similarity_rank_df(hotel_info_df, hotel_review_df, region, user_input):
    # 몇 개의 리뷰를 기준으로 할지
    review_number = 5

    # Pororo 사용 코드
    se = Pororo(task="sentence_embedding", lang="ko")
    user_input_vec = se(user_input)

    # 지역, label 필터링
    filtered_hotel_info_df = hotel_info_df[hotel_info_df['region'].isin(region)]
    positive_hotel_review_df = hotel_review_df[hotel_review_df['label'] == 1]
    filtered_hotel_review_df = positive_hotel_review_df[positive_hotel_review_df['hotel_id'].isin(filtered_hotel_info_df['hotel_id'])].copy()

    # similarity 계산
    print("start calculate similarity")
    start = time.time()

    process_num = 4
    with Pool(process_num) as p:
        range_review = len(filtered_hotel_review_df) // process_num
        ret1 = p.apply_async(get_similarity, (filtered_hotel_review_df[:range_review], user_input_vec))
        ret2 = p.apply_async(get_similarity, (filtered_hotel_review_df[range_review:range_review*2], user_input_vec))
        ret3 = p.apply_async(get_similarity, (filtered_hotel_review_df[range_review*2:range_review*3], user_input_vec))
        ret4 = p.apply_async(get_similarity, (filtered_hotel_review_df[range_review*3:], user_input_vec))
        filtered_hotel_review_df['similarity'] = pd.concat([ret1.get(), ret2.get(), ret3.get(), ret4.get()])
    
    print(f"end calculate similarity : {time.time() - start}")

    # hotel_id 별 top similarity review 추출
    top_hotel_review_df = filtered_hotel_review_df.sort_values(by='similarity', ascending=False).groupby('hotel_id').head(review_number)

    # similarity 평균을 사용해 hotel_id 정렬
    hotel_rank = top_hotel_review_df[['hotel_id', 'similarity']].groupby('hotel_id').mean().sort_values('similarity', ascending=False)

    return hotel_rank, top_hotel_review_df




def set_return_data(hotel_rank, top_hotel_review_df):
    return_data = []
    for itertuple in hotel_rank.itertuples():
        # hotel_rank groupby 하면서 hotel_id 가 index로 들어감
        hotel_id = itertuple.Index
        
        review_id_list = top_hotel_review_df[top_hotel_review_df['hotel_id'] == hotel_id]['review_id'].values
        review_id_list = [str(review_id) for review_id in review_id_list]
        similarity = round(itertuple.similarity[0][0] * 100, 1)

        hotel_dict = {}
        hotel_dict["hotel_id"] = str(hotel_id)
        hotel_dict['review_id'] = review_id_list
        hotel_dict['similarity'] = similarity

        return_data.append(hotel_dict)

    return return_data


# -------------------------

def get_recomended_hotel(region, user_input):
    try:
        hotel_review_df = pd.read_pickle('app/service/ai/review.pkl')
        hotel_info_df = pd.read_pickle('app/service/ai/info.pkl')

        hotel_rank, top_hotel_review_df = get_similarity_rank_df(hotel_info_df, hotel_review_df, region, user_input)

        # recomended_hotel을 백엔드에 전달하기 위해 변환
        return_data = set_return_data(hotel_rank, top_hotel_review_df)

        return return_data

    except Exception as e:
        print(e)
        return e
