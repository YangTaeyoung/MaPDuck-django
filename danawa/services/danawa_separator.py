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
        self.target_dict = dict() # 크롤링 후 출력할 dict

    def get_model_name(self, title_string: list):
        result_list = list() # 결과 후보군 생성
        title_list = self.kkma.pos(title_string)
        pattern = "^[A-Z0-9]+[A-Z0-9|(-)|(_)|(\/)][A-Z0-9]$"
        prog = re.compile(pattern)

        for title in title_list:
            if title[1] == "OL":
                if prog.fullmatch(title[0]) is not None and len(title[0]) >= 6:
                    result_list.append(title[0])

        for result in result_list:
            if result.find('-') != -1:
                return result
            elif result.find('/') != -1:
                return result
            elif result.find('_') != -1:
                return result

        if len(result_list) == 0:
            return None
        else:
            return result_list[0]
