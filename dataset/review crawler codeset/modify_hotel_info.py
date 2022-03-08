import os
import time
import math
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool

hotel_info_df = pd.read_csv('./dataset/final/hotel_info.csv')[:]
with webdriver.Chrome('C:/Users/Administrator/AppData/Local/Google/Chrome/chromedriver.exe') as driver:

    for itertuple in hotel_info_df.itertuples():
        region = itertuple.region
        hotel_id = itertuple.hotel_id
        hotel_name = itertuple.hotel_name
        hotel_link = itertuple.hotel_link
        driver.get(hotel_link)
        time.sleep(2)
   
        try:
            new_hotel_img_link = driver.find_element_by_css_selector('#hotel_main_content > div > div.clearfix.bh-photo-grid.bh-photo-grid--space-down.fix-score-hover-opacity > div:nth-child(3) > a').get_attribute('data-thumb-url')  
        except:
            try: 
                new_hotel_img_link = driver.find_element_by_css_selector('#hotel_main_content > div > div.clearfix.bh-photo-grid.fix-score-hover-opacity > div:nth-child(3) > a').get_attribute('data-thumb-url')
            except:
                try:
                    new_hotel_img_link = driver.find_element_by_css_selector('#hotel_main_content > div.clearfix.bh-photo-grid.bh-photo-grid--space-down.fix-score-hover-opacity > div:nth-child(3) > a').get_attribute('data-thumb-url')
                except:
                    new_hotel_img_link = driver.find_element_by_css_selector('#VRViewTab > div.bui-tab__content.bui-tab__content--selected > div > div.clearfix.bh-photo-grid.bh-photo-grid--space-down.fix-score-hover-opacity > div:nth-child(3) > a').get_attribute('data-thumb-url')
        
        hotel_address = driver.find_element_by_css_selector('#showMap2 > span.hp_address_subtitle.js-hp_address_subtitle.jq_tooltip').text

        info_df = pd.DataFrame(columns = ['region', 'hotel_id', 'hotel_name', 'address', 'hotel_link', 'img_link'])

        info_df.loc[0] = [region, hotel_id, hotel_name, hotel_address, hotel_link, new_hotel_img_link]

        info_df.to_csv(
            f'./dataset/final/final_hotel_info.csv',
            mode='a',
            encoding='utf-8-sig',
            header=False,
            index=False,
        )
# hotel_info_df['hotel_img_link'] = new_hotel_img_link_list
# hotel_info_df['address_list'] = hotel_address_list

# hotel_info_df.to_csv('./dataset/final/final_hotel_info.csv', encoding='utf-8-sig', index=False)