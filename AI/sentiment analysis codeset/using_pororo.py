import os
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"

# import library
import pandas as pd
from pororo import Pororo

# data load
review_df = pd.read_csv("train_data.csv")["review"]

documents = list(review_df)

df_label = pd.DataFrame(
        columns=[
            "review",
            "label"
        ]
    )

# model => nsmc ; 영화리뷰 / shopping ; 쇼핑몰리뷰
for doc in documents:
    posneg_classfier = Pororo(
        task="sentiment", model="brainbert.base.ko.nsmc", lang="ko"
    )
    result = posneg_classfier(str(doc))
    print(result)
    if result == "Positive":
        label = 1
    else:
        label = 0

    row = [doc, label]
    df_label.loc[len(df_label)] = row

df_label.to_csv("reveiw_label.csv")

if __name__ == "__main__":
    pass
