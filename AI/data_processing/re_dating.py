import pandas as pd

df = pd.read_csv("entire_hotel_review.csv", encoding="UTF-8")

date_list = list(df["date"])

new_date_list = []

for date in date_list:
    year = date[:4]

    if date[-2] == "0":
        new_date = f"{year}-10"
    elif date[-2] == "1":
        if date[-3] == "1":
            new_date = f"{year}-11"
        month = 1
        new_date = f"{year}-0{month}"
    elif date[-2] == "2":
        if date[-3] == "1":
            new_date = f"{year}-12"
        month = 2
        new_date = f"{year}-0{month}"
    else:
        month = date[-2]
        new_date = f"{year}-0{month}"

    new_date_list.append(new_date)
    pass


redate_df = pd.DataFrame({"redate": new_date_list})
redate_df.to_csv("redate_hotel_review.csv", header=True)

if __name__ == "__main__":
    pass