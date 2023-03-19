import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)

#basic browser operations in selenium
driver.maximize_window()
time.sleep(2)
print(driver.title)
print(driver.current_url)
driver.back()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.minimize_window()
time.sleep(2)
driver.close()

'''
# alert operations in selenium
testText = "Athithya"

driver.find_element(By.CSS_SELECTOR, "input[id='name']").send_keys("Athithya")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[id='alertbtn']").click()
time.sleep(2)
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
alert.accept()

assert testText in alertText
'''