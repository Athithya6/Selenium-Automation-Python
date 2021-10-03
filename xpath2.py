from selenium import webdriver

driver=webdriver.Chrome("D:\\Athithya\\chromedriver.exe")
driver.get("https://github.com/login")
driver.maximize_window()
#driver.find_element_by_xpath("//input[@id='login_field']").send_keys("Athithya6")
# identifying element
#driver.find_element_by_xpath("//a[text()='Forgot password?']").click()

# parent-child traverse tags
#driver.find_element_by_xpath("//div[@id='login']/div[4]/form/input[2]").send_keys("Athithya6")
#driver.find_element_by_xpath("//div[@id='login']/div[4]/form/div/input[1]").send_keys("Athithya$1997")
#driver.find_element_by_xpath("//div[@id='login']/div[4]/form/div/input[12]").click()

# checking parent-child traverse tags by printing label names
print(driver.find_element_by_xpath("//main[@id='js-pjax-container']/div/div[4]/form/label").text)
print(driver.find_element_by_xpath("//main[@id='js-pjax-container']/div/div[4]/form/div/label").text)