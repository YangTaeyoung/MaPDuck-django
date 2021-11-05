from django.urls import path
from . import views
urlpatterns = [
    path('myproducts/', views.MyProductView.as_view()),
]
