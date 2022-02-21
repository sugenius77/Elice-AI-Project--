import pandas as pd
import math
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
# from tqdm import tqdm


def get_reviews(cityname):

    global review_page
    region = []
    hotel_index = []
    hotel = []
    webpage = []
    review_positive = []
    review_negative = []
    date = []

    hotel_names = driver.find_elements_by_xpath('//*[@data-testid="title"]')
    hotel_links = driver.find_elements_by_css_selector(".fb01724e5b")
    hotel_name_list = []
    hotel_link_list = []
    for name, link in zip(hotel_names, hotel_links):
        name = name.text
        link = link.get_attribute("href")
        hotel_name_list.append(name)
        hotel_link_list.append(link)

    try:
        index = 0
        for i in range(len(hotel_name_list)):
            index += 1
            # 호텔 리스트와 클릭할 호텔의 이름이 같다면
            if (
                hotel_name_list[i]
                == driver.find_elements_by_xpath('//*[@data-testid="title"]')[i].text
            ):
                try:
                    # 체크인 날짜 팝업 끄기
                    driver.find_element_by_css_selector("#b2searchresultsPage").click()
                    # 호텔 클릭
                    driver.find_elements_by_xpath('//*[@data-testid="title"]')[i].click()
                    # 새로운 창을 핸들링
                    driver.switch_to.window(driver.window_handles[-1])
                    # 고객 후기 클릭
                    time.sleep(7)
                    driver.find_element_by_css_selector("#show_reviews_tab").click()
                except:
                    break
                # 한국어 리뷰만 보기
                try:
                    driver.find_element_by_css_selector(
                        "#review_lang_filter > button"
                    ).click()
                    driver.find_element_by_css_selector(
                        "#review_lang_filter > div > div > ul > li:nth-child(2) > button"
                    ).click()
                    time.sleep(5)
                    # 후기 가져오기
                    # 한국어 리뷰 수 가져와서 공백 제거
                    korean_review_raw = (
                        driver.find_element_by_xpath(
                            '//*[@id="review_lang_filter"]/div/div/ul/li[2]/button'
                        )
                        .get_attribute("textContent")
                        .replace(" ", "")
                    )
                    # 숫자만 슬라이싱
                    korean_review_num = korean_review_raw[8:-2]
                    review_page = math.ceil(int(korean_review_num) / 10)
                except:
                    pass

                j = 1
                time.sleep(3)
                while j < min(review_page, 12):
                    j += 1
                    for z in range(1, 10):
                        print(index, hotel_name_list[i])
                        region.append(cityname)
                        hotel_index.append(index)
                        hotel.append(hotel_name_list[i])
                        webpage.append(hotel_link_list[i])

                        # positive review
                        try:
                            review_positive.append(
                                driver.find_element_by_css_selector(
                                    f"#review_list_page_container > ul > li:nth-child({z}) > div > div.bui-grid > div.bui-grid__column-9.c-review-block__right > div:nth-child(2) > div > div:nth-child(1) > p > span.c-review__body"
                                ).get_attribute("textContent")
                            )
                        except:
                            review_positive.append(" ")
                        # negative review
                        try:
                            review_negative.append(
                                driver.find_element_by_css_selector(
                                    f"#review_list_page_container > ul > li:nth-child({z}) > div > div.bui-grid > div.bui-grid__column-9.c-review-block__right > div:nth-child(2) > div > div.c-review__row.lalala > p > span.c-review__body"
                                ).get_attribute("textContent")
                            )
                        except:
                            review_negative.append(" ")
                        # date
                        try:
                            date.append(
                                driver.find_element_by_css_selector(
                                    f"#review_list_page_container > ul > li:nth-child({z}) > div > div.bui-grid > div.bui-grid__column-3.c-review-block__left > ul.bui-list.bui-list--text.bui-list--icon.bui_font_caption.c-review-block__row.c-review-block__stay-date > li > div > span"
                                ).get_attribute("textContent")
                            )
                        except:
                            date.append(" ")
                    try:
                        time.sleep(2)
                        driver.find_element_by_xpath(
                            '//*[@id="review_list_page_container"]/div[4]/div/div[1]/div/div[3]/a'
                        ).click()
                    except:
                        break

            time.sleep(3)
            # 이전 창으로 핸들링
            driver.switch_to.window(driver.window_handles[0])
            pass

    finally:

        df = pd.DataFrame(
            {
                "date": date,
                "region": region,
                "hotel_index": hotel_index,
                "hotel_name": hotel,
                "hotel_link": webpage,
                "review_positive": review_positive,
                "review_negative": review_negative,
            }
        )

    return df


if __name__ == "__main__":

    final_df = pd.DataFrame(
        columns=[
            "date",
            "region",
            "hotel_index",
            "hotel_name",
            "hotel_link",
            "review_positive",
            "review_negative",
        ]
    )

    cityname_list = ["서울", "제주"]
    for cityname in cityname_list:

        options = webdriver.ChromeOptions()
        # options.add_argument("headless")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")

        # chromedriver path 지정
        driver = webdriver.Chrome(
            executable_path="/Users/taehyeonkim/chromedriver", options=options
        )

        token = cityname
        for page in range(0, 250, 25):
            url = f"http://booking.com/searchresults.ko.html?label=bdot-P2XUozRl7Uj73QAuByfkUwS267777897793%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-576851273475%3Alp1009871%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YUlRwjG4dAJkHxCuUKVzpFo&sid=6501b31231a00a3035b564f903cd02d3&aid=376440&sb_lp=1&src=index&error_url=https%3A%2F%2Fwww.booking.com%2Findex.ko.html%3Faid%3D376440%3Blabel%3Dbdot-P2XUozRl7Uj73QAuByfkUwS267777897793%253Apl%253Ata%253Ap1%253Ap22%252C563%252C000%253Aac%253Aap%253Aneg%253Afi%253Atikwd-576851273475%253Alp1009871%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YUlRwjG4dAJkHxCuUKVzpFo%3Bsid%3D6501b31231a00a3035b564f903cd02d3%3Bsb_price_type%3Dtotal%3Bsrpvid%3D7c2c0cadfaa9003e%26%3B&ss={token}&is_ski_area=0&checkin_year=&checkin_month=&checkout_year=&checkout_month=&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ss_raw={token}&search_pageview_id=a9d50caf10ae0098&nflt=class%3D3%3Bclass%3D5%3Bclass%3D4&offset={page}"
            driver.get(url)
            time.sleep(2)

            df = get_reviews(cityname)
            final_df = pd.concat([final_df, df], ignore_index=True)

            final_df.to_csv(
                f"{cityname}_hotel_review.csv",
                mode="a",
                encoding="utf-8-sig",
                header=False,
                index=False,
            )

            driver.quit()

    pass
