from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#username").send_keys("Athithya6")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Athithya$1997")

# static-drop down
s = Select(driver.find_element(By.CSS_SELECTOR, "select[class='form-control']"))
# s.select_by_visible_text("Student")
s.select_by_index(2)
# s.select_by_value("stud")

driver.find_element(By.XPATH, "//input[@id='terms']").click()
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
