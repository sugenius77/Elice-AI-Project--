from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import os.path

#차후 유지 보수 및 테스트를 위한 변수
url = 'https://booking.com' # url
region = '제주도' # 여행지
star_list = [3,4,5] # 몇성급 호텔을 검색 할지

review_num = None # 가져올 리뷰의 수
review_page_num = 200 # 가져올 리뷰 페이지 수 (전체 페이지수보다 크면 전체 페이지수로 변경됨)
hotel_num = None # 검색할 호텔의 수
hotel_page_num = 10 # 검색할 호텔 페이지 수

path = os.getcwd()

# 기본 페이지 호출 후 목적지로 검색 된 페이지 리턴
def get_searched_page(driver: webdriver, url:str, region: str, star_list: list) -> webdriver:
    # url 페이지 호출
    driver.get(url)
    driver.implicitly_wait(5)
    
    # 홈페이지에서 목적지 입력 태그와 버튼 태그 선택
    input_e = driver.find_element_by_id('ss')
    search_e = driver.find_element_by_class_name('sb-searchbox__button')

    # 목적지에 `region` 입력 후 버튼 클릭
    input_e.send_keys(region)
    search_e.click()

    # 호텔의 성급 필터링
    # class가 숫자 값으로 나와 지정하기 힘들다
    # xpath 사용 시 div 순서로만 찾아 '이전에 사용한 필터' 가 생기면 무용지물이 됨
    driver.implicitly_wait(5)
    
    star_filter_divs = driver.find_elements_by_xpath('//*[@id="searchboxInc"]//div')
    star_filter_inputs = []
    # id를 확인 할 수 있는 'searchboxInc' 아래 모든 div를 돌며 attribute가 'data-filters-group' == class 인지 확인
    for div in star_filter_divs:
        if div.get_attribute('data-filters-group') == 'class':
            star_filter_inputs = div.find_elements_by_tag_name('input')
            break

    # 성급 div내 input을 돌며 'name' attribute 확인
    for input_ in star_filter_inputs:
        star = int(input_.get_attribute('name')[-1])
        if star in star_list:
            input_.click() # click()으로 하면 다른 태그에 가려져 안되는 경우가 생김
            
    return driver

# 호텔 목록 페이지의 정보가 담김 driver를 받아 호텔의 링크 주소를 리스트 형태로 저장 후 리턴
def set_hotel_link_list(driver: webdriver, hotel_page_num: int) -> list:
    # 1페이지의 호텔 링크 리스트 생성 (기본이 1 페이지이므로 버튼 클릭 생략)
    time.sleep(5)
    hotel_div_a_all = driver.find_elements_by_xpath('//*[@id="search_results_table"]//a')
    for a in hotel_div_a_all:
        if a.get_attribute('data-testid') == 'title-link':
            with open(f'{path}\\link_file.txt', 'a') as f:
                f.write(f'{a.get_attribute("href")}\n')
    #hotel_link_list = [a.get_attribute('href') for a in hotel_div_a_all if a.get_attribute('data-testid') == 'title-link']
    
    # 페이지 네이션
    for i in range(1, hotel_page_num):
        nav = driver.find_element_by_xpath('//*[@id="search_results_table"]//nav')
        ol = nav.find_element_by_tag_name('ol')
        pages = ol.find_elements_by_tag_name('button')

        for page in pages:
            try:
                if i+1 == int(page.get_attribute('aria-label')):
                    page.click()
                    time.sleep(5) ## sleep이 없으면 페이지 갱신 전에 넘어감

                    # 검색 된 호텔 링크 리스트 추가
                    driver.implicitly_wait(5)

                    hotel_div_a_all = driver.find_elements_by_xpath('//*[@id="search_results_table"]//a')
                    for a in hotel_div_a_all:
                        if a.get_attribute('data-testid') == 'title-link':
                            with open(f'{path}\\link_file.txt', 'a') as f:
                                f.write(f'{a.get_attribute("href")}\n')
                    #hotel_link_list += [a.get_attribute('href') for a in hotel_div_a_all if a.get_attribute('data-testid') == 'title-link']
            except:
                print('ERROR in hotel_link page')
    #return hotel_link_list

# 호텔 정보를 csv로 저장
def set_hotels(driver: webdriver, hotel_link_list: list, hotel_num: int, review_num: int, review_page_num: int) -> pd.DataFrame:
    driver.implicitly_wait(3)

    review_file = f'./{region}_hotel_reviews.csv'
    
    # 링크를 돌며 리뷰 저장
    for index, link in enumerate(hotel_link_list[:hotel_num]):
        hotels = pd.DataFrame(columns=['region', 'name', 'room_type', 'date', 'review_title', 'review_great', 'review_poor', 'score'], dtype='str')

        driver.get(link)
        driver.implicitly_wait(3)

        # 호텔 이름 가져오기
        # a tag의 경우 .text가 아니라 get_attribute('text') 사용
        name = driver.find_element_by_id('hp_hotel_name_reviews').get_attribute('text')
        
        # 고객후기 탭 클릭
        review_tab = driver.find_element_by_id('show_reviews_tab')
        review_tab.click()
        time.sleep(3)

        # max_page 구하기
        pagenation_list = driver.find_element_by_class_name('bui-pagination__list')
        max_page = pagenation_list.find_elements_by_tag_name('a')
        max_page_num = int(max_page[-2].get_attribute('data-page-number'))
        review_page_num_temp = min(max_page_num, review_page_num)
        print(review_page_num_temp)

        # 이중 for문 탈출용
        flag = False
        # 페이지 네이션
        for i in range(review_page_num_temp):
            if flag:
                break
            # 실제 리뷰를 가져오는 부분. 리뷰도 페이지 네이션 되어 있는지 몰라서 함수화 못함. 차후 함수화, 페이지 네이션 코드 수정 필요
            # 리뷰 정보가 담긴 block 선택
            time.sleep(3)
            review_blocks = driver.find_elements_by_class_name('c-review-block')
            
            driver.implicitly_wait(3)
            pagenation_list = driver.find_element_by_class_name('bui-pagination__list')
            
            pages = pagenation_list.find_elements_by_tag_name('a')
            error_count = 0

            for block in review_blocks[:review_num]:
                
                driver.implicitly_wait(3)
                try:
                    # 리뷰 block은 left(정보), right(리뷰)로 나누어져 있음
                    block_left = block.find_element_by_class_name('c-review-block__left')
                    block_right = block.find_element_by_class_name('c-review-block__right')
                    
                    room_type = block_left.find_element_by_class_name('bui-list__body').text
                    date = block_left.find_element_by_class_name('c-review-block__date').text
                    review_title = block_right.find_element_by_class_name('c-review-block__title').text
                    score = block_right.find_element_by_class_name('bui-review-score__badge').text
                    
                    # 긍정 리뷰와 부정 리뷰를 나눔
                    review_great = ''
                    review_poor = ''
                    review_rows = block_right.find_elements_by_class_name('c-review__row')
                    driver.implicitly_wait(3)
                    for row in review_rows:
                        emotion = row.find_element_by_class_name('bui-u-sr-only').text
                
                        if emotion == '좋았던 점':
                            review_great = row.find_element_by_class_name('c-review__body').text
                        elif emotion == '아쉬웠던 점':
                            review_poor = row.find_element_by_class_name('c-review__body').text
                    
                    data = {'region' : region, 
                            'name' : name.rstrip().lstrip(), 
                            'room_type' : room_type, 
                            'date' : date, 
                            'review_title' : review_title, 
                            'review_great' : review_great.replace('\n', ' '), 
                            'review_poor' : review_poor.replace('\n', ' '), 
                            'score' : score}
                    hotels.loc[len(hotels)] = pd.Series(data=data, dtype=str)
                    print(data)

                except:
                    print('ERROR in review_page')
                    if error_count >= 2:
                        flag = True
                        break
                    error_count += 1

            for page in pages:
                if i+2 == int(page.get_attribute('data-page-number')):
                    print(f'************ hotel : {index+1} ************')
                    print(f'************ review : {i+1} page ************')
                    page.click()
                    time.sleep(2)
                    break
                
        
        hotels.to_csv(review_file, header=True if index == 0 else False, index=False, mode='a')

        # 호텔 하나 끝날 때 마다 csv에 저장
        #with open(review_file, mode = 'a') as f:
        #    hotels.to_csv(f, header=f.tell()==0, index=False)

# 동작 부분
with webdriver.Chrome('C:/Users/Administrator/AppData/Local/Google/Chrome/chromedriver.exe') as driver:
    link_file = f'{path}\\link_file.txt'
 
    if not os.path.isfile(link_file):
        # 기본 페이지 호출 후 목적지로 검색 된 페이지 리턴
        driver = get_searched_page(driver, url, region, star_list)
        # 호텔 목록 페이지의 정보가 담긴 driver를 받아 호텔의 링크 주소를 리스트 형태로 저장
        set_hotel_link_list(driver, hotel_page_num)

    hotel_link_list = []
    with open(link_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            hotel_link_list.append(line)

    # 호텔 링크 리스트를 받아 접속하여 호텔,리뷰 정보 저장
    set_hotels(driver, hotel_link_list, hotel_num, review_num, review_page_num)   
    