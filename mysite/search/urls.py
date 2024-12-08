from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_product, name='search_product'),  # 根路徑
]
