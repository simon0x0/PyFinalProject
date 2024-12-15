from django.shortcuts import render, redirect
from .models import Product
from .pchome_crawler import pchomeCrawler

# Create your views here.

product_list = []

def search_product(request):
    if request.method == 'POST':
        global product_list
        product_list = [] # 清空商品資訊
        query = request.POST.get('query')
        product_list = pchomeCrawler(query)
        return redirect(switch_page, page=1)
    return render(request, 'search/search.html')

def switch_page(request, page = 1):
    total_page = (len(product_list)+19)//20
    context = {
        'products': product_list[20*(page-1):min(20*page, len(product_list))], 
        'total_page': total_page,
        'page': page
    }
    return render(request, 'search/results.html', context)