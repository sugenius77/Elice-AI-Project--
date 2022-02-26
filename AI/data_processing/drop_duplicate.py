import pandas as pd
import numpy as np

# data load
df = pd.read_csv("hotel_review.csv", encoding="UTF-8")

print("initial: ", len(df["review"]))

# drop duplicates
df.drop_duplicates(["review"], keep="first", inplace=True)
print("drop duplicates: ", len(df["review"]))

df.to_csv("modified_hotel_review.csv")



if __name__ == "__main__":
    pass