import pandas as pd

from konlpy.tag import Okt

okt = Okt()


def build_bag_of_words(document):
    # 온점 제거 및 형태소 분석
    document = document.replace(".", "")
    tokenized_document = okt.morphs(document)

    word_to_index = {}
    bow = []

    for word in tokenized_document:
        if word not in word_to_index.keys():
            word_to_index[word] = len(word_to_index)
            # BoW에 전부 기본값 1을 넣는다.
            bow.insert(len(word_to_index) - 1, 1)
        else:
            # 재등장하는 단어의 인덱스
            index = word_to_index.get(word)
            # 재등장한 단어는 해당하는 인덱스의 위치에 1을 더한다.
            bow[index] = bow[index] + 1

    return word_to_index, bow


if __name__ == "__main__":
    tagged_review = pd.read_csv(
        "/Users/taehyeonkim/Desktop/EliceTrack/TeamProject[AI]/dataset/Tagged review.csv"
    )
    df_reviews = tagged_review["review_positive"]

    df_tokenized = pd.DataFrame(columns=["sentence", "vocabulary", "BoW"])

    for document in df_reviews:
        vocab, bow = build_bag_of_words(document)
        row = [document, vocab, bow]
        df_tokenized.loc[len(df_tokenized)] = row

    df_tokenized.to_csv("Tokenized review.csv")

    pass
