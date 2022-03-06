from pororo import Pororo
import pandas as pd

def posneg_classifier(token):
    classifier = Pororo(task="sentiment", model="brainbert.base.ko.shopping", lang="ko")
    result = classifier(token)
    return result


if __name__ == "__main__":

    wordcloud = pd.read_csv("wc_posneg.csv", encoding="UTF-8")
    id__ = list(wordcloud["hotel_id"])
    pos_wc = wordcloud["pos_wc"].tolist()
    neg_wc = wordcloud["neg_wc"].tolist()

    new_pos_wc = []
    new_neg_wc = []
    for i in range(0, len(id__)):
        positive = []
        negative = []
        try:
            pos_strings = pos_wc[i].split("'")
            neg_strings = neg_wc[i].split("'")
            for j in range(1, len(pos_strings), 2):
                positive.append(pos_strings[j])
            for k in range(1, len(neg_strings), 2):
                negative.append(neg_strings[k])
        except:
            positive.append("")
            negative.append("")
        new_pos_wc.append(positive)
        new_neg_wc.append(negative)
        pass

    for i in range(len(new_pos_wc)):
        print("positive", i)
        try:
            for j in range(len(new_pos_wc[i])):
                token = new_pos_wc[i][j]
                posneg_result = posneg_classifier(token)
                if posneg_result == "Negative":
                    new_pos_wc[i].pop(j)
                pass
        except:
            pass

    for i in range(len(new_neg_wc)):
        print("negative", i)
        try:
            for j in range(len(new_neg_wc[i])):
                token = new_neg_wc[i][j]
                posneg_result = posneg_classifier(token)
                if posneg_result == "Positive":
                    new_neg_wc[i].pop(j)
                pass
        except:
            pass

    filtered_wc = pd.DataFrame({"hotel_id": id__, "pos_wc": new_pos_wc, "neg_wc": new_neg_wc})

    filtered_wc.to_csv("filtered_wc_using_pororo.csv", mode="w", header=True)
    pass