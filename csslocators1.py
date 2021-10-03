from selenium import webdriver

driver = webdriver.Chrome("D:\\Athithya\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_css_selector("input[name='name']").send_keys("Athithya")
driver.find_element_by_css_selector("input[name='email']").send_keys("athithyanarayan@gmail.com")
driver.find_element_by_css_selector("input[id='exampleInputPassword1']").send_keys("Athithya$1997")
driver.find_element_by_css_selector("input[id='exampleCheck1']").click()
driver.find_element_by_css_selector("input[id='inlineRadio2']").click()
driver.find_element_by_css_selector("input[value='Submit']").click()

#grabbing and printing the successful message-standard way
#print(driver.find_element_by_class_name("alert-success").text)

#grabbing and printing the successful message using csslocator regex
print(driver.find_element_by_css_selector("div[class*='alert-success']").text)