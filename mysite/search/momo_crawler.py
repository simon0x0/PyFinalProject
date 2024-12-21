from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--disable-popup-blocking")
options.add_argument("--incognito")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

url = "https://www.momoshop.com.tw/"


def get_content(url):
    driver.get(url)
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='keyword']")),
        "Cannot find element",
    )
    search.send_keys("iphone")
    inputBtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='inputbtn']")),
        "Cannot find element",
    )
    inputBtn.click()
    # time.sleep(500)
    # wait data load using WebDriverWait
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='listArea']")),
        "Cannot find element",
    )
    soup = BeautifulSoup(driver.page_source, "html.parser")
    # find all  div with class goodsUrl
    for item in soup.find_all("div", class_="goodsUrl"):
        title = item.find("h3", class_="prdName").text
        price = item.find("span", class_="price").text
        img = item.find("img", class_="prdImg")["src"]
        print("Title: ", title, "Price: ", price, "Image: ", img, "\n")


get_content(url)