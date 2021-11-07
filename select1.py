from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
static_drop = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
static_drop.select_by_visible_text("Female")
# static_drop.select_by_index(1)




