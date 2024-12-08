import requests # 訪問網站
from bs4 import BeautifulSoup # 解析html
from .models import Product

def pchomeCrawler(query):
    query = query.replace(' ', '_')
    url = f'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={query}'
    header = { # 用來避免被反爬蟲的東西
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=header) # 訪問網站

    if response.status_code == 200: # 判斷是否能正常訪問網站
        data = response.json()
        totalPage = data['totalPage']
        cnt = 0
        product_list = []
        for _ in range(1, totalPage+1): # 每一頁
            newPage = url + f'&page={_}'
            response = requests.get(newPage, headers=header)
            data = response.json()['prods']
            for prod in data: # 每個商品
                product = Product.objects.create(
                    name = prod['name'],
                    price = prod['price'],
                    url = f'https://24h.pchome.com.tw/prod/{prod['Id']}'
                )
                product_list.append(product)
                cnt += 1
        print(cnt)
        return product_list
    else:
        print('There are something wrong.')

    # soup = BeautifulSoup(response.text, "html.parser") # 解析html
    # items = soup.find_all('li', class_ = 'c-listInfoGrid__item') # 找PChome的商品標籤

# for item in items:
#     item_name = item.find('div', class_='c-prodInfoV2__title')
#     item_price = item.find('div', class_='c-prodInfoV2__priceValue--m')
#     if item_name: # 找商品名稱
#         item_name = item_name['title']
#     if item_price: # 找商品價格
#         item_price = item_price.get_text(strip=True)
#     if item_name==None or item_price==None:
#         continue
#     print(f'商品名稱: {item_name} 商品價格: {item_price}')