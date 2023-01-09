from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

s_obj = ChromeService("C:\\Users\\Athithya Narayan\\Documents\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# user created xpaths
driver.find_element(By.NAME, "name").send_keys("Athithya Narayan")
driver.find_element(By.NAME, "email").send_keys("athithyanarayan@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Athithya$1997")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.ID, "inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@value='Submit']").click()

# cropath plugin xpath for submit button
# driver.find_element_by_xpath("//body/app-root[1]/form-comp[1]/div[1]/form[1]/input[1]").click()

# grabbing and printing the successful message-standard way
print(driver.find_element(By.CLASS_NAME, "alert-success").text)

# printing the successful message using xpath regex
# print(driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text)
