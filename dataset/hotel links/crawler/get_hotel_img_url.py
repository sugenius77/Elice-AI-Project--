import pandas as pd
import math
import time

from selenium import webdriver


def get_hotel_img_url(cityname):

    hotel_name_list = []
    hotel_img_link_list = []

    hotel_names = driver.find_elements_by_xpath('//*[@data-testid="title"]')
    hotel_img_links = driver.find_elements_by_xpath('//*[@data-testid="image"]')

    for name, img_link in zip(hotel_names, hotel_img_links):
        name = name.text
        img_link = img_link.get_attribute("src")
        hotel_name_list.append(name)
        hotel_img_link_list.append(img_link)


    df = pd.DataFrame(
        {
            "hotel_name": hotel_name_list,
            "hotel_img_url": hotel_img_link_list

        }
    )

    return df


if __name__ == "__main__":

    final_df = pd.DataFrame(
        columns=[
            "hotel_name",
            "hotel_img_url"
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

            df = get_hotel_img_url(cityname)
            final_df = pd.concat([final_df, df], ignore_index=True)

            final_df.to_csv(
                f"{cityname}_hotel_info_{page}.csv",
                mode="a",
                encoding="utf-8-sig",
                header=False,
                index=False,
            )

            driver.quit()

    pass
