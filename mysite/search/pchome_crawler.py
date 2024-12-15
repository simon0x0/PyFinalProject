import requests # 訪問網站
from bs4 import BeautifulSoup # 解析html
from .models import Product

def pchomeCrawler(query):
    query = query.replace(' ', '%20')
    url = f'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={query}'
    header = { # 用來避免被反爬蟲的東西
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=header) # 訪問網站

    if response.status_code == 200: # 判斷是否能正常訪問網站
        data = response.json()
        if len(data) == 0: # 找不到商品資料
            return []
        totalPage = data['totalPage']
        product_list = []
        for _ in range(1, totalPage+1): # 每一頁
            if _ >= 3: # 測試用
                break
            newPage = url + f'&page={_}'
            response = requests.get(newPage, headers=header)
            data = response.json()['prods']
            for prod in data: # 每個商品
                product = Product.objects.create(
                    name = prod['name'],
                    price = prod['price'],
                    url = f'https://24h.pchome.com.tw/prod/{prod['Id']}',
                    pic = 'https://img.pchome.com.tw/cs' + prod['picS']
                )
                product_list.append(product)
        return product_list
    else:
        print('There are something wrong.')