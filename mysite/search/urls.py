from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_product, name='search_product'),  # 根路徑
]

# urlpatterns += [
#     path('page/', views.switch_page, name='switch_page')
# ]
# urlpatterns += [
#     path('page/<int:page>/', views.switch_page, name='switch_page')
# ]

urlpatterns += [
    path('page/<int:page>/<int:order>/', views.switch_page, name='switch_page'),
    path('page/<int:page>/', views.switch_page, {'order': 1}, name='switch_page_default'),  # 默認升序
]
