# 작성자: 양태영
# 작성일: 21.10.30
# 입력: 문자열 리스트
# 반환: 문자열 리스트 중 가장 길이가 긴 요소
# 설명: 문자열 리스트 중 가장 길이가 긴 요소를 반환하는 함수
def len_max(str_list: list):
    if str_list:
        max_elem = str_list[0]
        for str in str_list[1:]:
            if len(str) > len(max_elem):
                max_elem = str
        return max_elem
    return -1

