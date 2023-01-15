import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.implicitly_wait(5)  # implicit wait- global wait; if next page resumes within 1.5 seconds instead of
# waiting for 5 seconds;
# if object does not come up at all, then webdriver waits for 10 seconds fully.

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ca")
wait = WebDriverWait(driver, 10)  # explicit wait
# time.sleep(5)
wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[class='products'] div h4")))

fruits = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(fruits)
assert count == 4
for fruit in fruits:
    fruit.find_element(By.XPATH, "div[3]/button").click() # chain the parent xpath in previous variable with the
    # child xpath here

# time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# time.sleep(5)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") # scrolling to bottom of page
driver.execute_script("window.scrollBy(0,350)", "")  # scrolling to bottom of page
driver.find_element(By.CSS_SELECTOR, "input.promoCode").send_keys("rahulshettyacademy")
# time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "button.promoBtn").click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)

orgAmt = driver.find_element(By.CSS_SELECTOR, "span.totAmt").text
disAmt = driver.find_element(By.CSS_SELECTOR, "span.discountAmt").text

assert int(orgAmt) > float(disAmt)
