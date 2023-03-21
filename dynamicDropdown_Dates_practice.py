import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")
for c in countries:
    if c.text=="India":
        c.click()
driver.find_element(By.ID, "ctl00_mainContent_rbtnl_Trip_1").click()
# driver.find_element(By.ID, "ctl00_mainContent_ddl_originStation1").send_keys("Che")
driver.find_element(By.ID, "ctl00_mainContent_ddl_originStation1_CTXT").click()
driver.find_element(By.XPATH, "//a[@value='MAA']").click()
# driver.find_element(By.ID, "ctl00_mainContent_ddl_destinationStation1_CTXT").send_keys("De")
driver.find_element(By.XPATH, "(//a[@value='DEL'])[2]").click()
driver.find_element(By.CSS_SELECTOR, "span[class*='ui-icon-circle-triangle-e']").click()
# time.sleep(10)
# driver.find_element(By.XPATH, "(//table[@class='ui-datepicker-calendar']/tbody/tr/td[6]/a)[1]").click()
driver.find_element(By.XPATH, "(//td[@data-month='4']/a)[5]").click()
driver.find_element(By.ID, "ctl00_mainContent_view_date2").click()
driver.find_element(By.CSS_SELECTOR, "span[class*='ui-icon-circle-triangle-e']").click()
# time.sleep(10)
# driver.find_element(By.XPATH, "(//table[@class='ui-datepicker-calendar']/tbody/tr/td[5]/a)[4]").click()
driver.find_element(By.XPATH, "(//td[@data-month='6']/a)[11]").click()
driver.find_element(By.ID, "ctl00_mainContent_chk_StudentDiscount").click()
select = Select(driver.find_element(By.ID, "ctl00_mainContent_DropDownListCurrency"))
select.select_by_value("USD")
driver.find_element(By.ID, "ctl00_mainContent_btn_FindFlights").click()
