import pandas as pd
import os

from konlpy.tag import Okt
from gensim.models.doc2vec import Doc2Vec, TaggedDocument


def cleansing(document):
    okt = Okt()

    # document normalization
    norm_doc = okt.normalize(document)
    token_list = okt.pos(norm_doc, join=True)
    targets = ["Adjective", "Adverb", "Noun", "Verb"]

    # targets에 해당되는 token만 추출해 저장
    doc_tokenized = []
    for token in token_list:
        for target in targets:
            if target in token:
                dash_index = token.index("/")
                doc_tokenized.append(token[0:dash_index])

    # stopwords 제거한 token 저장
    stop_words = "이	있 하 것 들 그 되 수 이 보 않 없 나 사람 주 아니 등 같 우리 때 년 가 한 지 대하 오 말 일 그렇 위하 때문 그것 두 말하 알 그러나 받 못하 일 그런 또 문제 더 사회 많 그리고 좋 크 따르 중 나오 가지 씨 시키 만들 지금 생각하 그러 속 하나 집 살 모르 적 월 데 자신 안 어떤 내 경우 명 생각 시간 그녀 다시 이런 앞 보이 번 나 다른 어떻 여자 개 전 들 사실 이렇 점 싶 말 정도 좀 원 잘 통하 소리 놓"
    stop_words = set(stop_words.split(" "))
    cleansed_doc = [word for word in doc_tokenized if not word in stop_words]

    return cleansed_doc


# 사용자 입력값을 토큰화 -> 벡터화 하고 유사도 높은 tag 데이터를 반환
def make_similar_docs(d2v_model, user_input):

    cleansed_test_target = cleansing(user_input)
    noun_user_input = cleansed_test_target

    # 유저 입력값의 벡터 생성
    user_input_vector = d2v_model.infer_vector(noun_user_input)

    # 유사도가 높은 리뷰 확인
    most_similar_docs = d2v_model.docvecs.most_similar(
        [user_input_vector], topn=len(d2v_model.docvecs))

    return most_similar_docs


def recomend_hotel(region, most_similar_docs):
    # 몇 개의 호텔을 추천할지
    number_top = 50

    # 몇 개의 리뷰를 기준으로 할지
    number_review = 4

    # similarity가 높은 순서대로 저장
    similar_review_hotel = pd.DataFrame(columns=['region', 'review_id', 'similarity', 'score', 'count'], dtype='object')

    for review, similarity in most_similar_docs:
        city, hotel_id, review_id = review.split("@")

        if city in region:
            if hotel_id not in similar_review_hotel.index:
                similar_review_hotel.loc[hotel_id] = [city, [review_id], [similarity], similarity, 1]
            
            elif similar_review_hotel.loc[hotel_id, 'count'] < number_review:
                    similar_review_hotel.loc[hotel_id, 'review_id'].append(review_id)
                    similar_review_hotel.loc[hotel_id, 'similarity'].append(similarity)
                    similar_review_hotel.loc[hotel_id, 'score'] += similarity
                    similar_review_hotel.loc[hotel_id, 'count'] += 1
            
            elif similar_review_hotel.loc[hotel_id, 'count'] >= number_review:
                pass  

        count_pass_hotel = similar_review_hotel.apply(lambda x: True if x['count'] >= number_review else False, axis=1).sum()
        
        if count_pass_hotel >= number_top:
            break

    # 호텔들을 similar_review list가 많은 순서대로 정렬
    recomended_hotel = similar_review_hotel.sort_values('score', ascending=False)

    return recomended_hotel


def show_recomended_hotel(hotel_info_df, hotel_review_df, return_data):
    # 추천된 호텔과 리뷰 확인

    for i in range(len(return_data)):

        hotel_id = return_data[i]['hotel_id']
        review_id_list = return_data[i]['review_id']
        print(hotel_id)
        print(review_id_list)
        print(f'----- {hotel_info_df.loc[int(hotel_id),"hotel_name"]} -----')

        for review_id in review_id_list[:len(return_data[-1]['review_id'])]:
            print(hotel_review_df.loc[int(review_id)]['contents'])
        print('')


def set_return_data(recomended_hotel):
    return_data = []
    for hotel in recomended_hotel.itertuples():
        hotel_id = hotel.Index
        region = hotel.region
        review_id_list = hotel.review_id
        similarity_list = hotel.similarity

        hotel_dict = {}
        hotel_dict["hotel_id"] = hotel_id
        hotel_dict["region"] = region
        hotel_dict['review_id'] = review_id_list
        hotel_dict['similarity'] = similarity_list

        return_data.append(hotel_dict)

    return return_data


# -------------------------

def get_recomended_hotel(region, user_input):

    # 모델을 로드 하고 로드 실패시 새로 생성
    try:
        print(os.getcwd())
        d2v_model = Doc2Vec.load('./AI/models/d2v.model')
        
    except Exception as e:
        print(e)
    
    most_similar_docs = make_similar_docs(d2v_model, user_input)
    
    recomended_hotel = recomend_hotel(region, most_similar_docs)
    
    # recomended_hotel을 백엔드에 전달하기 위해 변환
    return_data = set_return_data(recomended_hotel)
    
    #show_recomended_hotel(hotel_info_df, hotel_review_df, return_data) DB변화 후 에러로 주석

    return return_data
