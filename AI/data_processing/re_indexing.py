import pandas as pd

df = pd.read_csv("hotel_review.csv", encoding="UTF-8")

index_list = list(df["hotel_index"])

re_index_list = []
for index in index_list:
    re_index = 509
    re_index_list.append(re_index + index)
    pass

df = pd.DataFrame({"reindex": re_index_list})
df.to_csv("edit_sample.csv")

if __name__ == "__main__":
    pass
