import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
l = []

fv = {"Brocolli", "Cauliflower", "Carrot", "Tomato", "Beans", "Potato", "Onion", "Apple", "Grapes", "Banana", "Orange"}
products = driver.find_elements(By.CLASS_NAME, "product-name")
i = 0

for p in products:
    p1 = p.text.split("-")
    p2 = p1[0].strip()
    l.append(p2)

while i < len(l):
    if l.__getitem__(i) in fv:
        driver.find_elements(By.CSS_SELECTOR, "div.product-action").__getitem__(i).click()
        time.sleep(2)
    i += 1
