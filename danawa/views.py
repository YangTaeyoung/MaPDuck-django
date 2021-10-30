from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .services.crawling import DanawaCrawler
# Create your views here.

class Danawa(APIView):

    @swagger_auto_schema()
    def get(self, request):
        print("왔냐 씨발아")
        keyword = request.GET.get("keyword")
        danawa = DanawaCrawler()
        danawa.get_product_list_danawa(keyword, 10)
        print(danawa.products)
        for product in danawa.products:
            print(product.title)
            print(product.desc)
        return HttpResponse("hello")
