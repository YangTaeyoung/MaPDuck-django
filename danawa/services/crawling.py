#crawling
import requests
from bs4 import BeautifulSoup

# json
import json
from collections import OrderedDict

class DanawaCrawler:

    # to_json : list to json
    # product_name_list : 제품명 리스트
    # product_desc_list : 제품 스펙 리스트
    # num : len(product_name_list)
    def to_json(product_name_list, product_desc_list, num):
        data_list_json = OrderedDict()
        data_list = []

        for i in range(num):
            orderdict = OrderedDict()
            orderdict["prduct_num"] = i
            orderdict["product_name"] = product_name_list[i]
            orderdict["description"] = product_desc_list[i]

            data_list.append(orderdict)

        data_list_json["products"] = data_list
        json_data = json.dumps(data_list_json, ensure_ascii=False, indent="\t")

        return json_data

    # get_product_list_danawa : 검색 결과 크롤링
    # search : 검색어
    # end_page_num : 검색할 마지막 페이지
    def get_product_list_danawa(search, end_page_num):


        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        URL = "http://search.danawa.com/dsearch.php?query={}&originalQuery={}&volumeType=allvs&page={}&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=112757&defaultPhysicsCategoryCode=860%7C13735%7C14883%7C58972&defaultVmTab=27335&defaultVaTab=1412149&tab=goods"

        # 제품이름
        product_names = []
        # 제품 스펙
        product_desc = []
        # 페이지 시작 번호
        page_num = 1

        # crawling start
        while True:

            # end_page
            if page_num >= end_page_num:
                break

            url = URL.format(search, search, page_num)
            resp = requests.get(url, headers=headers)
            soup = BeautifulSoup(resp.text, "html.parser")

            # 제품 리스트
            product_list = soup.select(
                "#productListArea > div.main_prodlist.main_prodlist_list > ul.product_list > li")

            for i in range(len(product_list)):
                try:
                    product_names.append(product_list[i].select_one("div > div.prod_info > p > a").text)
                    desc_list = []
                    desc = product_list[i].select("div > dl.prod_spec_set > dd > div > a")
                    for j in range(len(desc)):
                        desc_list.append(desc[j].text)

                    product_desc.append(desc_list)

                except:
                    continue

            page_num += 1
            # crawling end

        # to_json
        products_json = DanawaCrawler.to_json(product_names, product_desc, len(product_names))

        return products_json




