from django.test import TestCase
from .services.naver_service import get_naver_shopping
# Create your tests here.

class NaverServiceTest(TestCase):
    def test_get_naver_api(self):
        res = get_naver_shopping("노트북")
        print(res)
