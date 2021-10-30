from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .services.crawling import DanawaCrawler
from .services.danawa_separator import DanawaSeparator
# Create your views here.

class Danawa(APIView):

    @swagger_auto_schema()
    def get(self, request):
        print("왔냐 씨발아")
        keyword = request.GET.get("keyword")
        danawa = DanawaCrawler()
        danawa.get_product_list_danawa(keyword, 2)
        danawa_separator = DanawaSeparator(danawa.products)
        products = danawa_separator.get_products()
        for product in products:
            print(f"모델명: {product.mo_name}")
            print(f"상품명: {product.pr_name}")
            print(f"설명: {product.desc}")
            print(f"이미지 경로: {product.img_path}")
        return HttpResponse("hello")
