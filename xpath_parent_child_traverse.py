import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s1 = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s1)
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.LINK_TEXT, "Forgot password?").click()

# parent-child traverse using xpath
driver.find_element(By.XPATH, "//div[@class='card-body mt-3']/div[2]/form/div[1]/input").send_keys("athithyanarayan@gmail.com")
driver.find_element(By.XPATH, "//div[@class='card-body mt-3']/div[2]/form/div[2]/input").send_keys("Athithya$1997")
driver.find_element(By.XPATH, "//div[@class='card-body mt-3']/div[2]/form/div[3]/input").send_keys("Athithya$1997")
driver.find_element(By.XPATH, "//div[@class='card-body mt-3']/div[2]/form/div[4]/button").click()
