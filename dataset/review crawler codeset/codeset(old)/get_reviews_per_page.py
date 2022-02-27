import pandas as pd
from selenium import webdriver

# 각 페이지 별 리뷰를 가져와 호텔 정보와 함께 하나의 리스트로 반환
def get_reviews_per_page(link):
    options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(executable_path="/Users/taehyeonkim/chromedriver", options=options)

    driver.get(link)
    driver.implicitly_wait(3)

    review_tab = driver.find_element_by_id('show_reviews_tab')
    review_tab.click()

    hotel_name = driver.find_element_by_id('hp_hotel_name').text
    review_score = driver.find_element_by_class_name('review-score-badge').text
    review_good = []
    review_bad = []

    review_divs = driver.find_elements_by_class_name('c-review')
    for div in review_divs[:50]:
        review_div_rows = div.find_elements_by_class_name('c-review__row')
        try:
            for row in review_div_rows:
                emotion = row.find_element_by_class_name('bui-u-sr-only').text

                if emotion == '좋았던 점':
                    review_good.append(row.find_element_by_class_name('c-review__body').text)
                elif emotion == '아쉬웠던 점':
                    review_bad.append(row.find_element_by_class_name('c-review__body').text)
        except:
            pass
    driver.quit()

    hotel_info = [hotel_name, review_score, review_good, review_bad]
    return hotel_info


if __name__ == "__main__":
    hotel_links = pd.read_csv("seoul_hotel_links")["hotel_link"]

    df_hotel_reviews = pd.DataFrame(
        columns=[
            "hotel_name",
            "hotel_score",
            "hotel_good_review",
            "hotel_bad_review"
        ]
    )

    for link in hotel_links:
        try:
            hotel_info = get_reviews_per_page(link)
            row = [hotel_info[0], hotel_info[1], hotel_info[2], hotel_info[3]]
            df_hotel_reviews.loc[len(df_hotel_reviews)] = row
        except:
            pass

    df_hotel_reviews.to_csv("seoul_hotel_reviews")
    pass






