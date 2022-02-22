import os
import time
import math
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool

def check_hotel_max_page(city_name):
    max_page = 10

    # 호텔 목록 페이지가 10 이하인 경우
    with webdriver.Chrome('C:/Users/Administrator/AppData/Local/Google/Chrome/chromedriver.exe') as driver:
        url = f"http://booking.com/searchresults.ko.html?label=bdot-P2XUozRl7Uj73QAuByfkUwS267777897793%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-576851273475%3Alp1009871%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YUlRwjG4dAJkHxCuUKVzpFo&sid=6501b31231a00a3035b564f903cd02d3&aid=376440&sb_lp=1&src=index&error_url=https%3A%2F%2Fwww.booking.com%2Findex.ko.html%3Faid%3D376440%3Blabel%3Dbdot-P2XUozRl7Uj73QAuByfkUwS267777897793%253Apl%253Ata%253Ap1%253Ap22%252C563%252C000%253Aac%253Aap%253Aneg%253Afi%253Atikwd-576851273475%253Alp1009871%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YUlRwjG4dAJkHxCuUKVzpFo%3Bsid%3D6501b31231a00a3035b564f903cd02d3%3Bsb_price_type%3Dtotal%3Bsrpvid%3D7c2c0cadfaa9003e%26%3B&ss={city_name}&is_ski_area=0&checkin_year=&checkin_month=&checkout_year=&checkout_month=&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ss_raw={city_name}&search_pageview_id=a9d50caf10ae0098&nflt=class%3D3%3Bclass%3D5%3Bclass%3D4&offset=0"
        driver.get(url)
        time.sleep(2)

        hotel_num = driver.find_element_by_css_selector('#search_results_table > div > div > div > div > div._b2280f5e6 > div._111b4b398').text.split()[-1][:-1]
        hotel_page = math.ceil(int(hotel_num) / 25)
        max_page = min(max_page, hotel_page)
    
    return max_page


def get_hotel_link(city_name, page):
    print(f'get_hotel_link Running on Process_{os.getpid()}')
    hotel_name_list = []
    hotel_link_list = []
    hotel_img_link_list = []

    with webdriver.Chrome('C:/Users/Administrator/AppData/Local/Google/Chrome/chromedriver.exe') as driver:
        url = f"http://booking.com/searchresults.ko.html?label=bdot-P2XUozRl7Uj73QAuByfkUwS267777897793%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-576851273475%3Alp1009871%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YUlRwjG4dAJkHxCuUKVzpFo&sid=6501b31231a00a3035b564f903cd02d3&aid=376440&sb_lp=1&src=index&error_url=https%3A%2F%2Fwww.booking.com%2Findex.ko.html%3Faid%3D376440%3Blabel%3Dbdot-P2XUozRl7Uj73QAuByfkUwS267777897793%253Apl%253Ata%253Ap1%253Ap22%252C563%252C000%253Aac%253Aap%253Aneg%253Afi%253Atikwd-576851273475%253Alp1009871%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YUlRwjG4dAJkHxCuUKVzpFo%3Bsid%3D6501b31231a00a3035b564f903cd02d3%3Bsb_price_type%3Dtotal%3Bsrpvid%3D7c2c0cadfaa9003e%26%3B&ss={city_name}&is_ski_area=0&checkin_year=&checkin_month=&checkout_year=&checkout_month=&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ss_raw={city_name}&search_pageview_id=a9d50caf10ae0098&nflt=class%3D3%3Bclass%3D5%3Bclass%3D4&offset={page}"    
        driver.get(url)
        time.sleep(2)

        hotel_names = driver.find_elements_by_xpath('//*[@data-testid="title"]')
        hotel_links = driver.find_elements_by_css_selector(".fb01724e5b")
        hotel_img_links = driver.find_elements_by_xpath('//*[@data-testid="image"]')

        for name, link, img_link in zip(hotel_names, hotel_links, hotel_img_links):
            name = name.text
            link = link.get_attribute("href")
            img_link = img_link.get_attribute("src")
            hotel_name_list.append(name)
            hotel_link_list.append(link)
            hotel_img_link_list.append(img_link)
        
    return hotel_name_list, hotel_link_list, hotel_img_link_list

def save_hotel_info(city_name, hotel_info: tuple):
    info_df = pd.DataFrame(columns = ['region', 'hotel_name', 'hotel_link', 'img_link'])
    for index in range(len(hotel_info[0])):
        name, link, img = hotel_info[0][index], hotel_info[1][index], hotel_info[2][index]
        info_df.loc[len(info_df)] = [city_name, name, link, img]
    
    info_df.to_csv(
        f'{city_name}_hotel_link.csv',
        mode='a',
        encoding='utf-8-sig',
        header=False,
        index=False,
    )


if __name__ == '__main__':
    process_num = 8

    city_name_list = ['서울', '제주', '부산', '강원도', '여수']
    #city_name_list = ['여수']
    for city_name in city_name_list:
        max_page = check_hotel_max_page(city_name)
        with Pool(process_num) as p:
            ret = p.starmap_async(get_hotel_link, [[city_name, page] for page in range(0, 25*max_page, 25)])
            ret_data = ret.get()
                    
        for data in ret_data:
            save_hotel_info(city_name, data)
        
    
        