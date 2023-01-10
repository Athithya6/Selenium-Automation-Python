import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s1 = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s1)
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.LINK_TEXT, "Forgot password?").click() #the web element must contain the anchor 'a' tag

# parent-child traverse using css
driver.find_element(By.CSS_SELECTOR, "div[class='card-body mt-3'] form div:nth-child(1) input")\
    .send_keys("athithyanarayan@gmail.com")
driver.find_element(By.CSS_SELECTOR, "div[class='card-body mt-3'] div form div:nth-child(2) input")\
    .send_keys("GermanyMS2022$#")
driver.find_element(By.CSS_SELECTOR, "div[class='card-body mt-3'] div form div:nth-child(3) input")\
    .send_keys("GermanyMS2022$#")
driver.find_element(By.CSS_SELECTOR, "div[class='card-body mt-3'] div form div:nth-child(4) button").click()


