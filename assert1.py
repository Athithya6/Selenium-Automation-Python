from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service

s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Kavitha Sreesaran")
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("kvsree1982@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[id='exampleInputPassword1']").send_keys("kv1982ET$#")

static_drop = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
static_drop.select_by_visible_text("Female")

driver.find_element(By.CSS_SELECTOR, "input[id='inlineRadio2']").click()

driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()

success_text = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
assert "success" in success_text