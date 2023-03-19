from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

# my solution
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()  # using regex in CSS
# driver.find_element(By.XPATH, "//a[contains(@href, 'shop')]").click() # using regex in XPath
l1 = []
items = driver.find_elements(By.CSS_SELECTOR, "div[class='card h-100'] div h4 a")
for i in range(0, len(items)):
    l1.append(items.__getitem__(i).text)
if 'Blackberry' in l1:
    driver.find_elements(By.CSS_SELECTOR, "div[class='card h-100'] div:nth-child(3) button").__getitem__(i).click()
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()


# Rahul's solution- using the concept of chaining to connect various XPath locators together
'''
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
'''

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

wait = WebDriverWait(driver, 10)
driver.find_element(By.CSS_SELECTOR, "input[id='country']").send_keys("ind")
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.CSS_SELECTOR, "div[class*='checkbox']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

successText = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
assert "Success! Thank you!" in successText
