from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radio_num = driver.find_elements(By.NAME, "radioButton")
# radio_num[2].click()

for r in radio_num:
    if r.get_attribute('value') == "radio1":
        r.click()

assert r.is_enabled()