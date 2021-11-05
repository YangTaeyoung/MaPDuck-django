class Naver:
    def __init__(self, title, company_name, img_path, purcharsed_at):
        self.title = title
        self.company_name = company_name
        self.img_path = img_path
        self.purchased_at = purcharsed_at

# 작성자: 양태영
# 작성일: 21.11.5
# 설명: 내 구매 목록 -> Spring 으로 돌려줄 때의 모델
class MyProduct:
    def __init__(self, mo_name, purchased_at):
        self.mo_name = mo_name
        self.purchased_at = purchased_at