from selenium import webdriver

driver = webdriver.Chrome("D:\\Athithya\\chromedriver.exe")
driver.get("https://github.com/login")
driver.maximize_window()
# new way of writing css locators specfically for ID and classname tags
# driver.find_element_by_css_selector("input#login_field").send_keys("Athithya6")
# driver.find_element_by_css_selector("input#password").send_keys("Athithya$1997")
# driver.find_element_by_css_selector("input#password").clear()   # to clear the password field
# driver.find_element_by_link_text("Forgot password?").click()  #works only if tagname is a(anchor)
# driver.find_element_by_css_selector("input.btn-block").click()

# parent-child traverse tags
print(driver.find_element_by_css_selector("main[id='js-pjax-container'] div:nth-child(1) div:nth-child(5) form label").text)
print(driver.find_element_by_css_selector("main[id='js-pjax-container'] div:nth-child(1) div:nth-child(5) form div label").text)
