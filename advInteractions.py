from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
exp_wait = WebDriverWait(driver, 5)  # explicit wait
driver.maximize_window()
a = ActionChains(driver)  # creating an object for actions class
a.move_to_element(driver.find_element(By.ID, "mousehover")).perform()  # for hovering over an item on the webpage
a.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()  # for performing right-clicks
exp_wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Reload")))  # explicit wait
a.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()  # for performing click using actions
