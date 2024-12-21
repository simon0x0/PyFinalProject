import requests # 訪問網站
from bs4 import BeautifulSoup # 解析html
import re
import json

# url = "https://www.momoshop.com.tw/search/searchShop.jsp?keyword=iphone"


def clean_json(json_str):
    # 移除陣列和物件中多餘的逗號
    json_str = re.sub(r",\s*([}\]])", r"\1", json_str)  # 移除 , 前面的多餘逗號
    return json_str


def get_content(url):

    header = { # 用來避免被反爬蟲的東西
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=header) # 訪問網站

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.find('script',type='application/ld+json').text
    text = clean_json(text)
    items = json.loads(text)["mainEntity"]["itemListElement"]
    print(items)
    # print(text.find("itemListElement"))
    # print(soup.find('script',type='application/ld+json').text)
    # print(response.text)
    # find all  div with class goodsUrl
    # print(soup.find_all("div", class_="goodsUrl"))
    for item in items:
        title = item["name"]
        url = item["url"]
        img = item["image"]
        price = item["offers"]["price"]
        print("Title: ", title, "Price: ", price, "Url: ", url, "Image: ", img, "\n")
