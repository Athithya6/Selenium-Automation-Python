import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
'''
driver.implicitly_wait(10) # global wait; if next page resumes within 1.5 seconds instead of waiting for 10 seconds;
# if object does not come up at all, then webdriver waits for 10 seconds fully.
'''

wait = WebDriverWait(driver,10) # explicit wait

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ca")
time.sleep(5)

'''
# fruits = driver.find_elements(By.XPATH, "//div[@class='products']/div")
# count = len(fruits)
# assert count == 4
'''

add_btns = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
for b in add_btns:
    b.click()

time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# time.sleep(5)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.promoCode")))
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") # scrolling to bottom of page
driver.execute_script("window.scrollBy(0,350)", "") # scrolling to bottom of page
driver.find_element(By.CSS_SELECTOR, "input.promoCode").send_keys("rahulshettyacademy")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "button.promoBtn").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)

