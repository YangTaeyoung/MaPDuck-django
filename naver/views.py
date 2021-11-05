from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from naver.services.naver_selenium_crawling import NaverCrawler
from naver.services.naver_service import get_my_products, get_naver_shopping
from naver.serializer import MyProductSerializer
from rest_framework.response import Response

# Create your views here.

# 내가 산 제품을 네이버에서 크롤링을 통해 얻는 함수
class MyProductView(APIView):
    @swagger_auto_schema()
    def get(self, request):
        id = request.META.get("HTTP_NAVER_ID")
        pw = request.META.get("HTTP_NAVER_PW")
        print(id)
        print(pw)
        naver_crawler = NaverCrawler()
        naver_crawler.get_prooduct_list_Naver(id, pw)
        my_product_list = get_my_products(naver_crawler.products)
        return Response(MyProductSerializer(data=my_product_list, many=True).data)


class NaverSearchView(APIView):
    @swagger_auto_schema()
    def get(self, request):
        keyword = request.GET.get("keyword")
        return get_naver_shopping(keyword)



