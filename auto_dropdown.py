import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(5)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))
for c in countries:
    if c.text=="India":
        c.click()
        break

print((driver.find_element(By.ID, "autosuggest")).text)
assert driver.find_element(By.ID, "autosuggest").get_attribute('value') == "India"
