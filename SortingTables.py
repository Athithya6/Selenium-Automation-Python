from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
# click on column header- this is browser sorting
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
browserSortedVeggies = []
originalSortedVeggies = []
# collecting all vegetables/fruits from the web page
veggieBrowserElements = driver.find_elements(By.XPATH, "//tr/td[1]")
# putting the collected elements in a list
for i in veggieBrowserElements:
    browserSortedVeggies.append(i.text)
# storing the collected elements in a new list
originalSortedVeggies = browserSortedVeggies.copy()
# python sort of browser sorted veggie elements list
browserSortedVeggies.sort()

assert browserSortedVeggies == originalSortedVeggies

