from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

radio_num = driver.find_elements(By.NAME, "radioButton")
r = radio_num[2]
r.click()

'''
for r in radio_num:
    if r.get_attribute('value') == "radio1":
        r.click()
'''
assert r.is_enabled()

# hide text box
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

