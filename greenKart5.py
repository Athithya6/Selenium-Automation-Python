import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
l1=[]
expected_list = ["Grapes","Orange", "Pomegranate", "Raspberry", "Strawberry"]
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ra")
time.sleep(5)
products = driver.find_elements(By.CSS_SELECTOR, "h4.product-name")
for p in products:
    s1 = p.text.split("-")
    s2 = s1[0].strip()
    l1.append(s2)

assert l1 == expected_list
