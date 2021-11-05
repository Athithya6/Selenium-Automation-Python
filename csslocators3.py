import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://mypage.rediff.com/login/dologin")

driver.find_element(By.CSS_SELECTOR, "div[id='leftcontainer'] div:nth-child(1) form div input").send_keys("Athithya6")
driver.find_element(By.CSS_SELECTOR, "div[id='leftcontainer'] div:nth-child(1) form:nth-child(5) div:nth-child(4) input:nth-child(4)").send_keys("Athithya$1997")
driver.find_element(By.CSS_SELECTOR, "div[id='pass_div'] input:nth-child(10)").click()
time.sleep(1000)

