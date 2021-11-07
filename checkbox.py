from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
print(len(checkboxes))
print(type(checkboxes))
print(checkboxes)

checkboxes[1].click()

# for c in checkboxes:
#    if c.get_attribute('value') == "option2":
#        c.click()

# assert c.is_selected()