from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
l1 = []
driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)

veg_fruits = ["Cucumber", "Beetroot", "Brinjal", "Capsicum", "Mushroom", "Pumpkin", "Mango", "Musk Melon", "Strawberry",
              "Almonds", "Cashews"]
extra_qty = [0, 1, 2, 0, 3, 0, 2, 0, 7, 1, 1]
prod = driver.find_elements(By.CSS_SELECTOR, "h4.product-name")
j = 0
m = 0

for k in prod:
    prod1 = k.text.split("-")
    prod2 = prod1[0].strip()
    l1.append(prod2)

for j in range(len(l1)):
    if l1.__getitem__(j) in veg_fruits:
        n = 0
        while n < extra_qty[m]:
            driver.find_elements(By.CSS_SELECTOR, "a.increment").__getitem__(j).click()
            # time.sleep(1)
            n += 1
        driver.find_elements(By.CSS_SELECTOR, "div.product-action").__getitem__(j).click()
        time.sleep(1)
        m += 1
driver.find_element(By.CSS_SELECTOR, "a.cart-icon").click()
driver.find_element(By.CSS_SELECTOR, "div.action-block").click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.promoCode")))
driver.find_element(By.CSS_SELECTOR, "input.promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, "button.promoBtn").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)
print("Total amount: " + driver.find_element(By.CSS_SELECTOR, "span.totAmt").text)
print("Total amount after discount: " + driver.find_element(By.CSS_SELECTOR, "span.discountAmt").text)
print("Discount %: " + driver.find_element(By.CSS_SELECTOR, "span.discountPerc").text)