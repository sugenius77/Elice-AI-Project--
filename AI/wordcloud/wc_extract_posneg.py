from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import *

import pandas as pd


def tfidf_wc(text):
    tfidf_v = TfidfVectorizer()
    tfidf_v.fit(text)
    vocab = tfidf_v.vocabulary_

    all = list(tfidf_v.transform(text).toarray())


    value_dict = {}
    for i in range(len(all)):
        for j in range(len(all[i])):
            value = all[i][j]
            if value != 0:
                value_dict[j] = value
        pass

    sorted_value = sorted(value_dict.items(), key=lambda item: item[1], reverse=True)
    # print(sorted_value)
    # print("=" * 100)


    key_list = []
    for i in range(len(sorted_value)):
        word_numb = sorted_value[i][0]
        for key, value in vocab.items():
            if value == word_numb:
                key_list.append(key)
        pass

    # print(key_list)
    # print("=" * 100)

    # key_list_noun = []
    # for key_ in key_list:
    #     okt = Okt()
    #     noun = okt.nouns(key_)
    #     key_list_noun.append(noun)
    #     pass

    # print(key_list_noun)
    # print("=" * 100)
    # return key_list_noun[:10]
    return key_list[:10]


if __name__ == "__main__":

    tagged_review = pd.read_csv("../wordcloud/final_hotel_review.csv", encoding="UTF-8")

    review_id_list = tagged_review["review_id"]
    hotel_id_list = tagged_review["hotel_id"]
    label_list = tagged_review["label"]

    review_set_list = []
    for i in range(len(review_id_list)):
        review_set = [review_id_list[i], hotel_id_list[i], label_list[i]]
        review_set_list.append(review_set)
        pass

    id_list = []
    corpus_pos_list = []
    corpus_neg_list = []
    for j in range(1, 552):
        id_list.append(j)
        corpus_pos = []
        corpus_neg = []
        for h in range(len(review_set_list)):
            try:
                if review_set_list[h][1] == j:
                    if review_set_list[h][2] == 1:
                        try:
                            review = tagged_review["review"][h]
                            corpus_pos.append(review)
                        except:
                            corpus_pos.append(" ")
                    else:
                        try:
                            review = tagged_review["review"][h]
                            corpus_neg.append(review)
                        except:
                            corpus_neg.append(" ")
            except:
                corpus_pos.append(" ")
                corpus_pos.append(" ")

        corpus_pos_list.append(corpus_pos)
        corpus_neg_list.append(corpus_neg)

        pass

    id__ = []
    wc_pos_list = []
    wc_neg_list = []
    for k in range(len(id_list)):
        id__.append(k + 1)
        try:
            wc_pos = tfidf_wc(text=corpus_pos_list[k])
            wc_neg = tfidf_wc(text=corpus_neg_list[k])
            wc_pos_list.append(wc_pos)
            wc_neg_list.append(wc_neg)
        except:
            wc_pos_list.append(" ")
            wc_neg_list.append(" ")
    pass

    df_wordcloud = pd.DataFrame({"hotel_id":id__, "pos_wc":wc_pos_list, "neg_wc":wc_neg_list})

    df_wordcloud.to_csv("wc_posneg.csv", mode="w", header=True)

    pass
