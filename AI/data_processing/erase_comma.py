import re
import pandas as pd

# data load
df = pd.read_csv("entire_hotel_review.csv", encoding="UTF-8")

reviews = list(df["review"])

new_reviews = []
for review in reviews:
    transformed = re.sub(",", "", review)
    new_reviews.append(transformed)
    pass

df = pd.DataFrame({"transformed_review": new_reviews})
df.to_csv("transformed_review.csv")


if __name__ == "__main__":
    pass