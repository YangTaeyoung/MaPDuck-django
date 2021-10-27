import requests
from bs4 import BeautifulSoup

class DanawaCrawler:

    # 함수화 해야함...(I'm sorry...)
    # 소스코드만 올리는데, 이거 장고에서 어떻게 실행해야할지(???)...
    # PR_NAMES: 제품명 , PR_DESCRIPTION: 제품 리스트

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    # 모니터 검색(예시) , 모니터 부분만 받아서 하면 될듯
    url = "http://search.danawa.com/dsearch.php?query=모니터&tab=main"

    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")

    # 제품 리스트
    PR_LIST = soup.select("#productListArea > div.main_prodlist.main_prodlist_list > ul.product_list > li")
    PR_NAMES = []  # 제품이름
    PR_DESCRIPTION = []  # 제품 스펙

    for i in range(len(PR_LIST)):
        try:
            PR_NAMES.append(PR_LIST[i].select_one("div > div.prod_info > p > a").text)

            desc_list = []
            desc = PR_LIST[i].select("div > dl.prod_spec_set > dd > div > a")
            for j in range(len(desc)):
                desc_list.append(desc[j].text)

            PR_DESCRIPTION.append(desc_list)
        except:
            continue


