from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

testText = "Athithya"

driver.find_element(By.CSS_SELECTOR, "input[id='name']").send_keys("Athithya")
driver.find_element(By.CSS_SELECTOR, "input[id='alertbtn']").click()
alert = driver.switch_to.alert
alertText = alert.text
alert.accept()

assert testText in alertText