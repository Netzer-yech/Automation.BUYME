import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:\\automation course\\chromedriver.exe"))
driver.get('https://buyme.co.il/')
driver.implicitly_wait(7)
driver.find_element(By.XPATH, value="//span[@tuafontsizes='14']").click()
driver.find_element(By.XPATH, value="//span[@andiallelmwithtext='16']").click()
print(driver.find_element(By.CSS_SELECTOR, value='input[id=ember2150]').is_displayed())

time.sleep(5)

