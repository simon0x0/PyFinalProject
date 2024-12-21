import requests
from bs4 import BeautifulSoup

url = 'https://tw.buy.yahoo.com/search/product?'
param = {'p': 'switch'} # 想要搜尋的商品名稱
header = { # 用來避免被反爬蟲的東西
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
response = requests.get(url, params=param, headers=header) # 訪問網站

if response.status_code == 200: # 判斷是否能正常訪問網站
    print(200)
else:
    print('There are something wrong.')
    
soup = BeautifulSoup(response.text, "html.parser") # 解析html

items = soup.find_all('div',class_='sc-1drl28c-2 ghwDyb')

for item in items:
    item_title = item.find('span', class_ = 'sc-hiOXk sc-itoVUi sc-1drl28c-5 eRihvI jcFejJ jZWZIY') 
    item_price = item.find('span', class_ = 'sc-hiOXk sc-itoVUi gnUMtx eZwHCZ')
    if item_title:
        item_title = item_title.get_text(strip=True)
    if item_price:
        item_price = item_price.get_text(strip=True)
    print(f'商品名稱: {item_title} 商品價格: {item_price}')