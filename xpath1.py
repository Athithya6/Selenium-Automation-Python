from selenium import webdriver

driver = webdriver.Chrome("D:\\Athithya\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

#user created xpaths
driver.find_element_by_xpath("//input[@name='name']").send_keys("Athithya")
driver.find_element_by_xpath("//input[@name='email']").send_keys("athithyanarayan@gmail.com")
driver.find_element_by_xpath("//input[@id='exampleInputPassword1']").send_keys("Athithya$1997")
driver.find_element_by_xpath("//input[@id='exampleCheck1']").click()
driver.find_element_by_xpath("//input[@id='inlineRadio2']").click()
#driver.find_element_by_xpath("//input[@value='Submit']").click()

#cropath plugin xpath for submit button
driver.find_element_by_xpath("//body/app-root[1]/form-comp[1]/div[1]/form[1]/input[1]").click()

#grabbing and printing the successful message-standard way
#print(driver.find_element_by_class_name("alert-success").text)

#printing the successful message using xpath regex
print(driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text)