from django.shortcuts import render
from .models import Product
from .pchome_crawler import pchomeCrawler
# Create your views here.

def search_product(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        product_list = pchomeCrawler(query)
        product_number = len(product_list)
        grouped_product_list = [] # 每20個分一組
        for i in range(0, product_number, 20):
            grouped_product_list.append(product_list[i: min(i+20, product_number)])
        context = {
            'products': grouped_product_list, 
            'group_number': len(grouped_product_list),
            'page': 1
        }
        return render(request, 'search/results.html', context)
    return render(request, 'search/search.html')

# def index(request):
#     context = {
#     }
#     return render(request, 'search/index.html', context)