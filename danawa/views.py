from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema


# Create your views here.

class Danawa(APIView):

    @swagger_auto_schema()
    def get(self, request):
        return HttpResponse("hello")
