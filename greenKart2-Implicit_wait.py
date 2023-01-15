import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.implicitly_wait(5) # implict wait- global wait; if next page resumes within 1.5 seconds instead of
# waiting for 5 seconds;
# if object does not come up at all, then webdriver waits for 10 seconds fully.

l=[]
l2=[]

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ca")
time.sleep(5) # This wait is important so that all the fruit and vegetable names beginning with ca are collected
# and stored in the fruits variable below. Implicit wait will not work on find on line 20.

fruits = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(fruits)
assert count == 4
for fruit in fruits:
    fruit.find_element(By.XPATH, "div[3]/button").click() # chain the parent xpath in previous variable with the
    # child xpath here

'''
add_btns = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
for b in add_btns:
    l.append(b.find_element(By.XPATH, "parent::div/parent::div/h4").text)
    b.click()
'''

# time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# time.sleep(5)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") # scrolling to bottom of page
driver.execute_script("window.scrollBy(0,800)", "") # scrolling to bottom of page
driver.find_element(By.CSS_SELECTOR, "input.promoCode").send_keys("rahulshettyacademy")
# time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "button.promoBtn").click()
driver.execute_script("window.scrollBy(0,800)", "")

vegetables = driver.find_elements(By.CSS_SELECTOR, "p.product-name")
for veg in vegetables:
    l2.append(veg.text)

# assert l==l2
print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)

