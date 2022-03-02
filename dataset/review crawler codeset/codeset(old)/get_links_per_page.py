import pandas as pd
from selenium import webdriver


# 각 페이지 별 호텔 링크를 가져와 하나의 리스트 형태로 반환
def get_links_per_page(cityid, citytype, pagenumb):
    # options = webdriver.ChromeOptions()
    # options.add_argument("headless")

    # driver = webdriver.Chrome(executable_path="/Users/taehyeonkim/chromedriver", chrome_options=options)
    driver = webdriver.Chrome(executable_path="/Users/taehyeonkim/chromedriver")

    url = f"https://www.booking.com/searchresults.ko.html?label=gen173nr-1DCAEoggI46AdIM1gEaH2IAQGYARe4AQfIAQzYAQPoAQGIAgGoAgO4As6Rj5AGwAIB0gIkZGUwMDlkZTAtYzAxNC00ZjllLTgwNzQtOGIwNmRkZWQ2ZWJm2AIE4AIB&sid=7648afe1e2b4ca4c6d0f1a854ed3a5bc&aid=304142&dest_id={cityid}&dest_type={citytype}&srpvid=38326b290a670a0f&nflt=class%3D4%3Bclass%3D3%3Bclass%3D5&offset={pagenumb}"
    driver.get(url)

    contents = driver.find_elements_by_xpath("//*[@id='search_results_table']//a")
    link_list = []
    for content in contents:
        if content.get_attribute("data-testid") == "title-link":
            link = content.get_attribute("href")
            link_list.append(link)

    driver.quit()

    return link_list


if __name__ == "__main__":
    df_hotel_links = pd.DataFrame(
        columns=[
            "page_numb",
            "hotel_link"
        ]
    )

    cityid = "900051692"
    citytype = "city"
    for pagenumb in range(0, 250, 25):
        link_list_per_page = get_links_per_page(cityid, citytype, pagenumb)
        for i in range(len(link_list_per_page)):
            row = [pagenumb, link_list_per_page[i]]
            df_hotel_links.loc[len(df_hotel_links)] = row
    df_hotel_links.to_csv("yeosu_hotel_links")
    pass
