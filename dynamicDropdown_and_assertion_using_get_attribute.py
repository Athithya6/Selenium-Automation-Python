import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

# dynamic drop-down
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(3)

# selecting India
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == 'India':
        country.click()
        break

# assertion for checking if IND has been typed correctly or not
# print(driver.find_element(By.ID, "autosuggest").text) # does not work because the text is not originally present
# in the test box of the website. .text will work only when text is originally present on the website
text_check = driver.find_element(By.ID, "autosuggest").get_attribute("value")  # get attribute is a Javascript method
# which loads the current text present in the textbox into the backend. This method will record the text selected
# by the user.
assert text_check == "India"
