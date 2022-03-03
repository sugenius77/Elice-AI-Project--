from sklearn.feature_extraction.text import TfidfVectorizer

import pandas as pd

tagged_review = pd.read_csv(
        "hotel_review.csv", encoding="UTF-8"
    )

corpus = list(tagged_review["review"])
labels = list(tagged_review["label"])


tfidfv = TfidfVectorizer().fit(corpus)
vocab = tfidfv.vocabulary_

# sorted_vocab = sorted(vocab.items(), key = lambda item: item[1], reverse = False)
# print(sorted_vocab)
# print("="*100)

all = list(tfidfv.transform(corpus).toarray())

value_dict = {}
for i in range(len(all)):
    for j in range(len(all[i])):
        value = all[i][j]
        if value != 0:
            value_dict[j] = value
    pass

sorted_value = sorted(value_dict.items(), key = lambda item: item[1], reverse = True)
print(sorted_value)
print("="*100)


key_list = []
for i in range(len(sorted_value)):
    word_numb = sorted_value[i][0]
    for key, value in vocab.items():
        if value == word_numb:
            key_list.append(key)
    pass

print(key_list)
print("="*100)


if __name__ == "__main__":
    pass