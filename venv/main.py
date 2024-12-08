import requests # 訪問網站
from bs4 import BeautifulSoup # 解析html

url = 'https://24h.pchome.com.tw/search/'
param = {'q': 'switch'} # 想要搜尋的商品名稱
header = { # 用來避免被反爬蟲的東西
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
response = requests.get(url, params=param, headers=header) # 訪問網站

if response.status_code == 200: # 判斷是否能正常訪問網站
    print(200)
else:
    print('There are something wrong.')

soup = BeautifulSoup(response.text, "html.parser") # 解析html
items = soup.find_all('li', class_ = 'c-listInfoGrid__item') # 找PChome的商品標籤

for item in items:
    item_name = item.find('div', class_='c-prodInfoV2__title')
    item_price = item.find('div', class_='c-prodInfoV2__priceValue--m')
    if item_name: # 找商品名稱
        item_name = item_name['title']
    if item_price: # 找商品價格
        item_price = item_price.get_text(strip=True)
    if item_name==None or item_price==None:
        continue
    print(f'商品名稱: {item_name} 商品價格: {item_price}')