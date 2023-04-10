import time

from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


chrome_option = Options()
chrome_option.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service("C:\\automation course\\chromedriver.exe"), options=chrome_option)
action = ActionChains(driver)
time_out = 10
wait = WebDriverWait(driver, time_out)

driver.get('https://buyme.co.il/money/370060?price=250')
driver.find_element(By.XPATH, value="//div[@gtm='למישהו אחר']").click()
driver.find_element(By.XPATH, value="//input[@maxlength='25']").send_keys('daniel gotlib')
event = Select(driver.find_element(By.NAME, value='eventType'))
wait.until(ec.element_to_be_clickable(event.select_by_index(3)))
time.sleep(5)








# class Constants():
#
# class SenderReceiver(BasePage):
#
#     def __init__(self, driver):
#         BasePage.__init__(self, driver)