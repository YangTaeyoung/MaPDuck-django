from django.urls import path
from . import views
urlpatterns = [
    path('products/', views.Danawa.as_view()),
]
