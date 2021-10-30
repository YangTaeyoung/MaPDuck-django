# crawling
import requests
from bs4 import BeautifulSoup

# json
import json
from collections import OrderedDict

from ..dto import Danawa

class DanawaCrawler:

    def __init__(self):
        self.products = list()

    def get_product_list_danawa(self, search, end_page_num):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        URL = "http://search.danawa.com/dsearch.php?query={}&originalQuery={}&volumeType=allvs&page={}&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=112757&defaultPhysicsCategoryCode=860%7C13735%7C14883%7C58972&defaultVmTab=27335&defaultVaTab=1412149&tab=goods"

        # 페이지 시작 번호
        page_num = 1

        # crawling start
        while True:

            # end_page
            if page_num > end_page_num:
                break

            url = URL.format(search, search, page_num)
            resp = requests.get(url, headers=headers)
            soup = BeautifulSoup(resp.text, "html.parser")

            # 제품 리스트
            product_list = soup.select("#productListArea > div.main_prodlist.main_prodlist_list > ul.product_list > li")

            for i in range(len(product_list)):

                try:
                    # title
                    title = product_list[i].select_one("div > div.prod_info > p > a").text

                    # image
                    try:
                        img_path = product_list[i].select_one("div > div.thumb_image > a > img")["src"]
                    except KeyError:
                        img_path = product_list[i].select_one("div > div.thumb_image > a > img")["data-original"]

                    # desc
                    desc_list = []
                    desc = product_list[i].select("div > dl.prod_spec_set > dd > div > a")
                    for j in range(len(desc)):
                        desc_list.append(desc[j].text)

                    desc = '/'.join(desc_list)

                    # desc end
                    self.products.append(Danawa(title, desc, img_path))

                except AttributeError:
                    continue

            page_num += 1
