import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.execute_script("window.scrollTo(0,450);")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screenshot1.png")