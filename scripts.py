import time
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:\\automation course\\chromedriver.exe"))
driver.get('https://buyme.co.il/')
driver.implicitly_wait(3)
driver.find_element(By.XPATH, value="//span[@tuafontsizes='14']").click()
my_button = driver.find_element(By.CSS_SELECTOR, value='h1[class=bm-h1]')
driver.find_element(locate_with(By.TAG_NAME, 'span').below(my_button)).click()
driver.find_element(By.CSS_SELECTOR, value='input[class=ember-view ember-text-field]').send_keys('netzer')

time.sleep(5)


