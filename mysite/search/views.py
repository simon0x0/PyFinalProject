from django.shortcuts import render, redirect
from .models import Product
from .pchome_crawler import pchomeCrawler

# Create your views here.


product_list = []


def asorder(x):
    return x.price

def search_product(request):
    if request.method == 'POST':
        global product_list
        product_list = [] # 清空商品資訊
        query = request.POST.get('query')
        product_list = pchomeCrawler(query)

        min_price = request.POST.get('min_price', '')
        max_price = request.POST.get('max_price', '')
        if min_price and max_price:
            product_list = [product for product in product_list if product.price >= int(min_price) and product.price <= int(max_price)]
        elif min_price:
            product_list = [product for product in product_list if product.price >= int(min_price)]
        elif max_price:
            product_list = [product for product in product_list if product.price <= int(max_price)]

        product_list.sort(key=asorder)
        return redirect(switch_page, page=1)
    return render(request, 'search/search.html')

def switch_page(request, page = 1):
    total_page = (len(product_list)+19)//20
    # 取得頁數參數，並將其限制在有效範圍內
    try:
        page = int(request.GET.get('page', page))
        if page < 1:
            page = 1
        elif page > total_page:
            page = total_page
    except ValueError:
        page = 1  # 如果頁數無效，默認為第 1 頁

    context = {
        'products': product_list[20*(page-1):min(20*page, len(product_list))], 
        'total_page': total_page,
        'page': page
    }
    return render(request, 'search/results.html', context)