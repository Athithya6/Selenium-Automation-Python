from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Athithya Narayan")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("athithyanarayan@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").send_keys("Athithya$1997")
driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()

# static_dropdown- if select tag is present next to a webelement, use Select class
sel = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
sel.select_by_index(0)
# sel.select_by_visible_text("Male")

driver.find_element(By.XPATH, "//input[@value='Submit']").click()

