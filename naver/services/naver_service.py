import requests
from ..dto import Naver, MyProduct
from danawa.services.danawa_separator import DanawaSeparator
# 작성자: 양태영
# 작성일: 21.11.03
# 입력: query: 검색어
# 반환: naver api결과 리스트 객체
# 설명: 검색어(query)를 통해 네이버 쇼핑리스트를 조회하고 반환하는 것.
def get_naver_shopping(query):
    url = "https://openapi.naver.com/v1/search/shop.json"
    headers = {
        "X-Naver-Client-Id": "9JWI6ruL74CEVqgkzXzE",
        "X-Naver-Client-Secret": "FJYLc07Kas"
    }
    return requests.get(url=url, headers=headers, params={"query": query}).json().get("items")


def get_my_products(navers: list):
    for naver in navers:
        danawa_separator = DanawaSeparator(dict())
        my_product_list = list()
        for naver in navers:
            purchased_at = naver.purchased_at
            temp, title_str = danawa_separator.get_company_id(naver.title)
            mo_name, title_str = danawa_separator.get_model_name(title_str)
            if mo_name is None:
                continue
            my_product_list.append(MyProduct(mo_name, purchased_at))
    return my_product_list