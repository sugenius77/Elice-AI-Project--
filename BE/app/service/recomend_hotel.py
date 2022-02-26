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


# review_list를 가져와서 명사만 추출한 후 tag(index)와 함께 tagged_corpus_list에 저장
def tag_corpus(hotel_review_df):

    tagged_corpus_list = []

    for df in hotel_review_df.itertuples():

        index = df.Index
        review_id = df.review_id
        hotel_id = df.hotel_id
        review = df.contents

        cleansed_doc = cleansing(review)

        try:
            tagged_line = TaggedDocument(
                tags=[f'{hotel_id}@{review_id}'], words=cleansed_doc)
            tagged_corpus_list.append(tagged_line)
        except Exception as e:
            print('Error in tagged_corpus')
            continue
        print(f'---{round((index / len(hotel_review_df)) * 100 ,3)}%---')

    return tagged_corpus_list


def make_model(tagged_corpus_list):

    # 모델 생성
    d2v_model = Doc2Vec(vector_size=300, window=3, workers=8,
                        min_count=len(tagged_corpus_list) // 1000)

    # 단어 빌드
    d2v_model.build_vocab(tagged_corpus_list)

    # 학습
    d2v_model.train(tagged_corpus_list,
                    total_examples=d2v_model.corpus_count, epochs=30)

    # 저장
    d2v_model.save('../AI/models/d2v.model')

    # 로드
    #d2v_model = Doc2Vec.load('../AI/models/d2v.model')

    return d2v_model


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


def recomend_hotel(most_similar_docs):
    # 몇 개의 호텔을 추천할지
    number_top = 100
    # 몇 개의 리뷰를 기준으로 할지
    number_review = 4
    # list의 길이를 기준으로 정렬하기 위해 Series 사용
    similar_review_hotel = pd.Series([], dtype='object')

    # 초기값 설정
    count_pass_hotel = 0

    for review, similarity in most_similar_docs:
        hotel, index = review.split("@")

        if hotel not in similar_review_hotel:
            similar_review_hotel[hotel] = [index]
        else:
            similar_review_hotel[hotel].append(index)

        if len(similar_review_hotel[hotel]) == number_review:
            count_pass_hotel += 1
        if count_pass_hotel >= number_top:
            break

    # 호텔들을 similar_review list가 많은 순서대로 정렬
    recomended_hotel = similar_review_hotel.sort_values(
        key=lambda x: x.str.len(), ascending=False).head(number_top)

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

    for hotel_id, review_id_list in recomended_hotel.items():
        hotel_dict = {}
        hotel_dict["hotel_id"] = hotel_id
        hotel_dict['review_id'] = []

        for review_id in review_id_list[:len(recomended_hotel[-1])]:
            # print(review_id)
            hotel_dict['review_id'].append(review_id)

        return_data.append(hotel_dict)

    return return_data


# -------------------------

def get_recomended_hotel(hotel_info_df, hotel_review_df, user_input):

    # hotel_review.csv 파일 내 column 변경 (나중에 제거 필요)
    #hotel_review_df.rename(columns={'hotel_index': 'hotel_id'}, inplace=True)

    # 모델을 로드 하고 로드 실패시 새로 생성
    try:
        print(os.getcwd())
        d2v_model = Doc2Vec.load('../AI/models/d2v.model')

    except Exception as e:
        print(e)
        tagged_corpus_list = tag_corpus(hotel_review_df)
        # 너무 길거나 짧은 리뷰 제거
        filtered_tagged_corpus_list = [x for x in tagged_corpus_list if (
            len(x[0]) >= 5) and (len(x[0]) <= 100)]

        d2v_model = make_model(tagged_corpus_list)
    print("통과1")
    most_similar_docs = make_similar_docs(d2v_model, user_input)
    print("통과2")
    recomended_hotel = recomend_hotel(most_similar_docs)
    print("통과3")
    # recomended_hotel을 백엔드에 전달하기 위해 변환
    return_data = set_return_data(recomended_hotel)
    print("통과4")
    # show_recomended_hotel(hotel_info_df, hotel_review_df, return_data) DB변화 후 에러로 주석

    return return_data
