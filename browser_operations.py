import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

s = ChromeService("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
time.sleep(2)
driver.maximize_window()
driver.get("https://tu-dresden.de/")
print(driver.title)
print(driver.current_url)
driver.get("https://www.tu-chemnitz.de/index.html.en")
print(driver.current_url)
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.minimize_window()
time.sleep(2)
driver.close()