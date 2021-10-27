from konlpy.tag import Kkma
from konlpy.utils import pprint
import re


# 작성자: 양태영
# 설명: 크롤러를 통해 받은 내용을 재분리하여 spring에 맞는 dict형식으로 보내기 위한 것.

class DanawaSeparator:
    kkma = Kkma()

    def __init__(self, danawa_dict):
        # 크롤링을 통해 분리된 dict: json/danawa.json형식
        self.products = danawa_dict.get("products")
        # 크롤링 후 출력할 딕셔너리
        self.target_dict = {
            "products": list(),
            'product_num': int()
        }

        # 작성자: 양태영

    # 작성일: 21.10.27
    # 설명 title에서 모델명 추출하는 함수 추출 실패시 None 도출
    # INPUT: 제목
    # RETURN: 모델명 or None
    def get_model_name(self, title_string: list):
        result_list = list()  # 결과 후보군 생성
        title_list = self.kkma.pos(title_string)
        # 모델명 판별 패턴 설정
        pattern = "^[A-Z0-9]+[A-Z0-9|(-)|(_)|(\/)][A-Z0-9]$"
        prog = re.compile(pattern)

        for title in title_list:
            if title[1] == "OL":
                if prog.fullmatch(title[0]) is not None and len(title[0]) >= 6:
                    result_list.append(title[0])

        # 모델명 찾기 실패
        if len(result_list) == 0:
            return None

        # 모델명에 요소가 있는 경우 유력 후보 탐색
        # 탐색 기준 string속에 -, /, _ 문자가 포함되어 있는가?
        # 있을 경우 모델명일 확률이 높기 때문에 해당 문자열을 바로 리턴함
        for result in result_list:
            if result.find('-') != -1:
                return result
            elif result.find('/') != -1:
                return result
            elif result.find('_') != -1:
                return result

        # 없을 경우 결과 후보군 중 가장 첫번째 요소를 리턴함.
        return result_list[0]

    def get_warranty(self, title, description):
        return 0

    # Spring에 보낼 필요한 요소를 포장하여 내보내는 함수.
    def get_target_dict(self):
        for product in self.products:
            # 모델명이 없으면 상품파악이 불가능해지므로 쓰지 않음.
            if model_name := self.get_model_name(product.get("title")):
                product_dict = dict()
                product_dict["model_name"] = model_name
                product_dict["description"] = product["description"]
                product_dict["warranty"] = self.get_warranty(product.get("title"), product.get("description"))
                product_dict["img_path"] = product["img_path"]
                self.target_dict["products"].append(product_dict)
