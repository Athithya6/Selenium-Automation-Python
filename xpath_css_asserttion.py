import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

s_obj = ChromeService("C:\\Users\\Athithya Narayan\\Documents\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# xpath and css locators
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Athithya")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("athithyanarayan@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[id='exampleInputPassword1']").send_keys("Athithya$1997 ")
driver.find_element(By.XPATH, "//input[@id='exampleCheck1']").click()
driver.find_element(By.CSS_SELECTOR, "input[id='inlineRadio1']").click()
driver.find_element(By.XPATH, "//input[@value='Submit']").click()
time.sleep(3)
# alert_mes = driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']").text
alert_mes = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
print(alert_mes)

# assert command to verify if alert message was printed correctly or not
assert "Success" in alert_mes

#cropath plugin xpath for submit button
# driver.find_element_by_xpath("//body/app-root[1]/form-comp[1]/div[1]/form[1]/input[1]").click()

#printing the successful message using xpath regex
# print(driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text)