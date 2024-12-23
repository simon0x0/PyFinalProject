import re
import json
import requests # 訪問網站
from bs4 import BeautifulSoup # 解析html
from .models import Product


def clean_json(json_str):
    # 移除陣列和物件中多餘的逗號
    json_str = re.sub(r",\s*([}\]])", r"\1", json_str)  # 移除 , 前面的多餘逗號
    return json_str


def get_content(key):
    url = f"https://www.momoshop.com.tw/search/searchShop.jsp?keyword={key}"
    header = { # 用來避免被反爬蟲的東西
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=header) # 訪問網站

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.find('script',type='application/ld+json').text
    text = clean_json(text)
    items = json.loads(text)["mainEntity"]["itemListElement"]
    # print(items)
    product_list = []
    for item in items:
        # print("Title: ", title, "Price: ", price, "Url: ", url, "Image: ", img, "\n")
        product = Product.objects.create(
            name = item["name"],
            price = int(item["offers"]["price"]),
            url = item["url"],
            pic = item["image"]
        )
        product_list.append(product)
    return product_list
