from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

s = Service("C:\\Users\\Athithya Narayan\\Desktop\\Athithya\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
''' My solution
red_text = driver.find_element(By.CSS_SELECTOR, "p.im-para.red").text
print(red_text)
text_1 = red_text.split("@")
text_2 = text_1[0].split()
text_3 = text_1[1].split()
email = text_2[4] + '@' + text_3[0]
print(email)
'''

'''Rahul's solution
message = driver.find_element(By.CSS_SELECTOR, ".red").text
# var = message.split("at")[1].strip().split(" ")[0]
print(var)
'''

driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys("Athithya$1997")
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "signInBtn").click()

wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, "div.alert-danger").text)


