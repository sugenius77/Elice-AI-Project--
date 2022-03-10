import pandas as pd
import time
import os

from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool


def get_latest_review(hotel_info_df, start_id, end_id):
    # 1달 전 최신 리뷰 가져오기
    filtered_hotel_info = hotel_info_df[(hotel_info_df['hotel_id'] >= start_id) & (hotel_info_df['hotel_id'] <= end_id)].copy()

    with webdriver.Chrome('C:/Users/Administrator/AppData/Local/Google/Chrome/chromedriver.exe') as driver:
        driver.get('https://www.booking.com/index.ko.html?label=gen173nr-1DCAEoggI46AdIM1gEaH2IAQGYARe4ARfIAQzYAQPoAQGIAgGoAgO4Av-rlJEGwAIB0gIkZGQyZGViZGEtMjRhZC00ODdmLWE5ZTMtZjYwZGM4NjI5MTFm2AIE4AIB;sid=c07843c4ec1b2207a50b02e715c87648;keep_landing=1&sb_price_type=total&')
        time.sleep(2)

        for itertuple in filtered_hotel_info.itertuples():
            url = itertuple.hotel_link
            hotel_id = itertuple.hotel_id

            driver.get(url)
            time.sleep(2)

            # # 고객후기 탭 클릭
            # review_tab = driver.find_element_by_id('show_reviews_tab')
            # review_tab.click()
            # time.sleep(2)

            # # 한국어 리뷰만 보기
            # try:
            #     driver.find_element_by_css_selector('#review_lang_filter > button').click()
            #     driver.find_element_by_css_selector('#review_lang_filter > div > div > ul > li:nth-child(2) > button').click()
            #     time.sleep(2)
            # except Exception as e:
            #     print(hotel_id)
            #     print(e)
            #     continue

            # # 최근 후기부터로 정렬
            # driver.find_element_by_xpath('//*[@id="review_sort"]').click()
            # driver.find_element_by_xpath('//*[@id="review_sort"]/option[2]').click()
            # time.sleep(2)

            # try:
            #     pagenation_list = driver.find_element_by_class_name('bui-pagination__list')
            
            # except Exception as e:
            #     print(hotel_id)
            #     print(e)
            #     continue

            # max_page = pagenation_list.find_elements_by_tag_name('a')
            # max_page_num = int(max_page[-2].get_attribute('data-page-number'))
            
            # break_flag = 0

            # # 리뷰 가져오기
            # for i in range(max_page_num):
            #     if break_flag == 1:
            #         break               
                
            #     review_blocks = driver.find_elements_by_class_name('c-review-block')
            #     pagenation_list = driver.find_element_by_class_name('bui-pagination__list')
            #     pages = pagenation_list.find_elements_by_tag_name('a')

            #     for block in review_blocks:
            #         try:
            #             pagenation_list = driver.find_element_by_class_name('bui-pagination__list')
            #             pages = pagenation_list.find_elements_by_tag_name('a')
                        
            #             block_left = block.find_element_by_class_name('c-review-block__left')
            #             block_right = block.find_element_by_class_name('c-review-block__right')

            #             user_id = block_left.find_element_by_class_name('bui-avatar-block__title').text
            #             str_check_date = block_right.find_element_by_class_name('c-review-block__date').text
            #             str_review_date = block_left.find_element_by_class_name('c-review-block__date').text

            #             check_year = str_check_date.split()[2][:-1]
            #             check_month = str_check_date.split()[3][:-1]
                        
            #             review_year = str_review_date.split()[-2][:-1]
            #             review_month = str_review_date.split()[-1][:-1]
            #             review_date = review_year + '-' + review_month
                        
            #             year = date.today().year
            #             month = date.today().month
            #             month = month if month is not 1 else 13
                        
            #             reviews = block_right.find_elements_by_class_name('c-review__body')

            #             if int(check_month) + 1 == month:
            #                 for review in reviews:
            #                     text = review.text.replace(',', ' ').replace('\n', ' ')
            #                     if text == '작성한 내용이 없습니다':
            #                         pass
            #                     else:
            #                         with open('latest_review.csv', mode='a', encoding='UTF-8-sig') as f:
            #                             f.write(f'{review_date},{user_id},{text},{hotel_id}\n')
                        
            #             elif (int(check_month) + 1 < month) or (int(check_year) < year):
            #                 break_flag = 1
            #                 break

            #         except Exception as e:
            #             print(e)
                
            #     for page in pages:
            #         if i+2 == int(page.get_attribute('data-page-number')):
            #             print(f'************{os.getpid()} hotel : {hotel_id} ************')
            #             print(f'************ review : {i+1} page ************')
            #             page.click()
            #             time.sleep(2)
            #             break

    return 'success'


if __name__ == '__main__':
    hotel_info_df = pd.read_csv('./dataset/final/final_hotel_info.csv')
    hotel_review_df = pd.read_csv('./dataset/final/final_hotel_review.csv')

    process_num = 4
    end = 546
    start = [x for x in range(1, end, 100)]

    latest_review = get_latest_review(hotel_info_df, 1, end)    

    # with Pool(process_num) as p:
    #     ret1 = p.apply_async(get_latest_review, (hotel_info_df, start[0], start[0] ))
    #     ret2 = p.apply_async(get_latest_review, (hotel_info_df, start[1], start[1] ))
    #     ret3 = p.apply_async(get_latest_review, (hotel_info_df, start[2], start[2] ))
    #     ret4 = p.apply_async(get_latest_review, (hotel_info_df, start[3], start[3] ))
    #     ret5 = p.apply_async(get_latest_review, (hotel_info_df, start[4], start[4] ))
    #     ret6 = p.apply_async(get_latest_review, (hotel_info_df, start[5], end))
        
    #     ret_list = []
    #     ret_list.append(ret1.get())
    #     ret_list.append(ret2.get())
    #     ret_list.append(ret3.get())
    #     ret_list.append(ret4.get())
    #     ret_list.append(ret5.get())
    #     ret_list.append(ret6.get())
        
    #     latest_review = pd.concat(ret_list, axis=0)
    
    
        