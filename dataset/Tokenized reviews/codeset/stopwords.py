from konlpy.tag import Okt
from PyKomoran import *

import pandas as pd

okt = Okt()
komoran = Komoran("STABLE")


def remove_stopwords(document):
    target_tags = ["NNP", "NNG", "VV", "VA", "EC"]
    cleansed_list = komoran.get_morphes_by_tags(document, tag_list=target_tags)

    stop_words = "이	있 하 것 들 그 되 수 이 보 않 없 나 사람 주 아니 등 같 우리 때 년 가 한 지 대하 오 말 일 그렇 위하 때문 그것 두 말하 알 그러나 받 못하 일 그런 또 문제 더 사회 많 그리고 좋 크 따르 중 나오 가지 씨 시키 만들 지금 생각하 그러 속 하나 집 살 모르 적 월 데 자신 안 어떤 내 경우 명 생각 시간 그녀 다시 이런 앞 보이 번 나 다른 어떻 여자 개 전 들 사실 이렇 점 싶 말 정도 좀 원 잘 통하 소리 놓"

    stop_words = set(stop_words.split(" "))

    result = [word for word in cleansed_list if not word in stop_words]

    return cleansed_list, result

def cleansing_wo_komoran(document):
    # okt.tagset => 품사확인

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


if __name__ == "__main__":

    tagged_review = pd.read_csv(
        "/Users/taehyeonkim/Desktop/EliceTrack/TeamProject[AI]/dataset/Tagged review.csv"
    )
    df_reviews = tagged_review["review_positive"]

    df_cleansing = pd.DataFrame(
        columns=["sentence", "cleansed_target", "cleansed_stopwords"]
    )

    df_cleansing_wo_komoran = pd.DataFrame(
        columns=["sentence", "cleansed_data"]
    )

    for document in df_reviews:

        # cleansed_target, cleansed_stopwords = remove_stopwords(document)
        # row = [document, cleansed_target, cleansed_stopwords]
        # df_cleansing.loc[len(df_cleansing)] = row

        cleansed_data = cleansing_wo_komoran(document)
        row2 = [document, cleansed_data]
        df_cleansing_wo_komoran.loc[len(df_cleansing_wo_komoran)] = row2

    # df_cleansing.to_csv("Cleansing review.csv")
    # df_cleansing_wo_komoran.to_csv("Cleansing review without komoran")

    pass
