import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s1 = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s1)
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
time.sleep(5)

# Registration at the website
'''
driver.find_element(By.CSS_SELECTOR, ".btn1").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Athithya")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#lastName").send_keys("Narayan")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("athithyanarayan@gmail.com")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[id='userMobile']").send_keys("9176459239")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='Male']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[id='userPassword']").send_keys("Athithya$1997")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='confirmPassword']").send_keys("Athithya$1997")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='Register']").click()
'''

'''
# logging in
driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("athithyanarayan@gmail.com")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='userPassword']").send_keys("Athithya$1997")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"#login").click()
time.sleep(5)
driver.find_element(By.XPATH, "(//button[@class='btn btn-custom'])[4]").click()
time.sleep(5)
driver.minimize_window()
time.sleep(3)
driver.close()
'''


driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("athithyanarayan@gmail.com")
driver.find_element(By.XPATH, "//input[@id='userPassword']").send_keys("Athithya$1997")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Athithya$1997")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
