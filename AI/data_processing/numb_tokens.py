import pandas as pd
from nltk.tokenize import word_tokenize

df = pd.read_csv("data/강원도_hotel_review.csv", encoding="UTF-8")

documents = list(df["review"])
indicies = list(df["review_index"])


index_list = []
for doc, index in zip(documents, indicies):
    str_doc = str(doc)
    numb_tokens = len(word_tokenize(str_doc))
    if numb_tokens <= 2 or numb_tokens > 250:
        index_list.append(int(index))
    pass

new_df = df.drop(index_list)

new_df.to_csv("data/edit_강원도_hotel_review.csv", header=False)

if __name__ == "__main__":
    pass
