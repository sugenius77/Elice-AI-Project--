import pandas as pd
import math
import time

from selenium import webdriver
from tqdm import tqdm


def get_reviews(cityname):

    global review_page
    region = []
    hotel = []
    review_title = []
    review_positive = []
    review_negative = []
    room_type = []
    date = []
    score = []

    options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        executable_path="/Users/taehyeonkim/chromedriver", options=options
    )

    # TODO 페이지 별로 url 다르게 넣어줘야 함
    # 필터링 된 url
    token = cityname
    url = f"http://booking.com/searchresults.ko.html?label=bdot-P2XUozRl7Uj73QAuByfkUwS267777897793%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-576851273475%3Alp1009871%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YUlRwjG4dAJkHxCuUKVzpFo&sid=6501b31231a00a3035b564f903cd02d3&aid=376440&sb_lp=1&src=index&error_url=https%3A%2F%2Fwww.booking.com%2Findex.ko.html%3Faid%3D376440%3Blabel%3Dbdot-P2XUozRl7Uj73QAuByfkUwS267777897793%253Apl%253Ata%253Ap1%253Ap22%252C563%252C000%253Aac%253Aap%253Aneg%253Afi%253Atikwd-576851273475%253Alp1009871%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YUlRwjG4dAJkHxCuUKVzpFo%3Bsid%3D6501b31231a00a3035b564f903cd02d3%3Bsb_price_type%3Dtotal%3Bsrpvid%3D7c2c0cadfaa9003e%26%3B&ss={token}&is_ski_area=0&checkin_year=&checkin_month=&checkout_year=&checkout_month=&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ss_raw={token}&search_pageview_id=a9d50caf10ae0098&nflt=class%3D3%3Bclass%3D5%3Bclass%3D4"
    driver.get(url)
    time.sleep(2)

    hotel_name = driver.find_elements_by_xpath('//*[@data-testid="title"]')
    hotel_name_list = []
    for name in hotel_name:
        name = name.text
        hotel_name_list.append(name)

    hotel_page_raw = (
        driver.find_element_by_css_selector(
            "#search_results_table > div:nth-child(1) > div > div > div > div._b2280f5e6 > div._111b4b398"
        )
        .get_attribute("textContent")
        .replace(" ", "")
    )

    # TODO: 슬라이싱 바꿔주기
    hotel_page = math.ceil(int(hotel_page_raw[9:-1]) / 25)

    try:
        for k in tqdm(range(0, hotel_page)):
            time.sleep(3)
            for i in tqdm(range(len(hotel_name_list))):
                # 호텔 리스트와 클릭할 호텔의 이름이 같다면
                if (
                    hotel_name_list[i]
                    == driver.find_elements_by_xpath('//*[@data-testid="title"]')[
                        i
                    ].text
                ):
                    # 체크인 날짜 팝업 끄기
                    driver.find_element_by_css_selector("#b2searchresultsPage").click()
                    # 호텔 클릭
                    driver.find_elements_by_xpath('//*[@data-testid="title"]')[
                        i
                    ].click()
                    # 새로운 창을 핸들링
                    driver.switch_to.window(driver.window_handles[-1])
                    # 고객 후기 클릭
                    time.sleep(7)
                    driver.find_element_by_css_selector("#show_reviews_tab").click()
                    # 한국어 리뷰만 보기
                    try:
                        driver.find_element_by_css_selector(
                            "#review_lang_filter > button"
                        ).click()
                        driver.find_element_by_css_selector(
                            "#review_lang_filter > div > div > ul > li:nth-child(2) > button"
                        ).click()
                        time.sleep(5)
                        ## 후기 가져오기
                        # 한국어 리뷰 수 가져와서 공백 제거 ex) 한국어  (45)
                        korean_review_raw = (
                            driver.find_element_by_xpath(
                                '//*[@id="review_lang_filter"]/div/div/ul/li[2]/button'
                            )
                            .get_attribute("textContent")
                            .replace(" ", "")
                        )
                        # 숫자만 슬라이싱
                        korean_review_num = korean_review_raw[8:-2]
                        print(korean_review_num)
                        review_page = math.ceil(int(korean_review_num) / 10)
                    except:
                        pass
                    for j in tqdm(range(0, review_page)):
                        time.sleep(3)
                        for z in tqdm(range(1, 11)):
                            # TODO 해당 지역으로 이름을 바꿔줘야 함
                            region.append(cityname)
                            hotel.append(hotel_name_list[i])
                            try:
                                review_title.append(
                                    driver.find_element_by_css_selector(
                                        f"#review_list_page_container > ul > li:nth-child({z}) > div > div.bui-grid > div.bui-grid__column-9.c-review-block__right > div:nth-child(1) > div > div.bui-grid__column-10 > h3"
                                    ).get_attribute("textContent")
                                )
                            except:
                                review_title.append(None)
                            try:
                                review_positive.append(
                                    driver.find_element_by_css_selector(
                                        f"#review_list_page_container > ul > li:nth-child({z}) > div > div.bui-grid > div.bui-grid__column-9.c-review-block__right > div:nth-child(2) > div > div:nth-child(1) > p > span.c-review__body"
                                    ).get_attribute("textContent")
                                )
                            except:
                                review_positive.append(None)
                            try:
                                review_negative.append(
                                    driver.find_element_by_css_selector(
                                        f"#review_list_page_container > ul > li:nth-child({z}) > div > div.bui-grid > div.bui-grid__column-9.c-review-block__right > div:nth-child(2) > div > div.c-review__row.lalala > p > span.c-review__body"
                                    ).get_attribute("textContent")
                                )
                            except:
                                review_negative.append(None)
                            try:
                                room_type.append(
                                    driver.find_element_by_css_selector(
                                        f"#review_list_page_container > ul > li:nth-child({z}) > div > div.bui-grid > div.bui-grid__column-3.c-review-block__left > div.c-review-block__row.c-review-block__room-info-row.review-block__room-info--disabled > ul > li > a > div"
                                    ).get_attribute("textContent")
                                )
                            except:
                                room_type.append(None)
                            try:
                                date.append(
                                    driver.find_element_by_css_selector(
                                        f"#review_list_page_container > ul > li:nth-child({z}) > div > div.bui-grid > div.bui-grid__column-3.c-review-block__left > ul.bui-list.bui-list--text.bui-list--icon.bui_font_caption.c-review-block__row.c-review-block__stay-date > li > div > span"
                                    ).get_attribute("textContent")
                                )
                            except:
                                date.append(None)
                            try:
                                score.append(
                                    driver.find_element_by_css_selector(
                                        f"#review_list_page_container > ul > li:nth-child({z}) > div > div.bui-grid > div.bui-grid__column-9.c-review-block__right > div:nth-child(1) > div > div.bui-grid__column-2.bui-u-text-right > div > div"
                                    ).get_attribute("textContent")
                                )
                            except:
                                score.append(None)
                                # 후기 다음 페이지
                        try:
                            driver.find_element_by_xpath(
                                '//*[@id="review_list_page_container"]/div[4]/div/div[1]/div/div[3]/a'
                            ).click()
                        except:
                            driver.switch_to.window(driver.window_handles[0])
                time.sleep(3)
                # 이전 창으로 핸들링
                driver.switch_to.window(driver.window_handles[0])
            driver.find_element_by_xpath(
                '//*[@id="search_results_table"]/div/div/div/div/div[7]/div[2]/nav/div/div[3]/button'
            ).click()

    finally:

        df = pd.DataFrame(
            {
                "date": date,
                "region": region,
                "hotel": hotel,
                "room_type": room_type,
                "score": score,
                "review_title": review_title,
                "review_positive": review_positive,
                "review_negative": review_negative,
            }
        )

        df.to_csv(
            f"{cityname}_review.csv",
            mode="a",
            encoding="utf-8-sig",
            header=False,
            index=False,
        )

    return df


if __name__ == "__main__":
    # cityname_list = ["서울", "부산", "제주", "여수", "강원"]
    cityname_list = ["서울"]
    for cityname in cityname_list:
        df_reviews = get_reviews(cityname)
    pass
