from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
testText = "Athithya"

driver.find_element(By.CSS_SELECTOR, "input[id='name']").send_keys("Athithya")
driver.find_element(By.CSS_SELECTOR, "input[id='alertbtn']").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
alert.accept()
# alert.dismiss()

assert testText in alertText