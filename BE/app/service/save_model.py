from konlpy.tag import Okt
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import pandas as pd
import os


def cleansing(document, pos):
    okt = Okt()

    # document normalization
    norm_doc = okt.normalize(document)
    token_list = okt.pos(norm_doc, join=True)
    targets = pos
    #targets = ["Adjective", "Adverb", "Noun", "Verb"]

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


# review_list를 가져와서 형태소 추출 후 tag(region, hotel_id)와 함께 tagged_corpus_list에 저장
def tag_corpus(hotel_info_df, hotel_review_df, pos):
    positive_hotel_review_df = hotel_review_df[hotel_review_df['label'] == 1]
    reindex_hotel_info_df = hotel_info_df.set_index('hotel_id')
    tagged_corpus_list = []

    print(f'start tagging pid : {os.getpid()}')
    for df in positive_hotel_review_df.itertuples():
        index = df.Index
        review_id = df.review_id
        hotel_id = df.hotel_id
        review = df.contents

        try:
            region = reindex_hotel_info_df.loc[hotel_id]['region']
            cleansed_doc = cleansing(review, pos)
            tagged_line = TaggedDocument(
                tags=[f'{region}@{hotel_id}@{review_id}'], words=cleansed_doc)
            tagged_corpus_list.append(tagged_line)
        except Exception as e:
            print('Error in tagged_corpus', e)
            continue
        #print(f'---{round((index / len(hotel_review_df)) * 100 ,3)}%---')

    return tagged_corpus_list


def make_model(model_name, tagged_corpus_list, window, min_count, epochs):
    # 모델 생성
    d2v_model = Doc2Vec(vector_size=300, window=window, workers=8,
                        min_count=len(tagged_corpus_list) // min_count)
    # 단어 빌드
    print(f"start model build pid : {os.getpid()}")
    d2v_model.build_vocab(tagged_corpus_list)
    # 학습
    print(f"start training pid : {os.getpid()}")
    d2v_model.train(tagged_corpus_list,
                    total_examples=d2v_model.corpus_count, epochs=epochs)
    # 저장
    d2v_model.save(f'app/service/ai/{model_name}.model')

    return model_name


def save_model(hotel_info_df, hotel_review_df, model_name, pos, token_min, token_max, window, min_count, epochs):
    try:
        tagged_corpus_list = tag_corpus(hotel_info_df, hotel_review_df, pos)
        # 너무 길거나 짧은 리뷰 제거
        filtered_tagged_corpus_list = [x for x in tagged_corpus_list if (
            len(x[0]) >= token_min) and (len(x[0]) <= token_max)]

        model_name = make_model(
            model_name, filtered_tagged_corpus_list, window, min_count, epochs)
    except Exception as e:
        print(e)
        return(f'{model_name} save fail')

    return f"{model_name} save success"
