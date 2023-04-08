from base_page import BasePage
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException

chrome_option = Options()
chrome_option.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service("C:\\automation course\\chromedriver.exe"), options=chrome_option)
driver.get('https://buyme.co.il/search?budget=3&category=16&region=11')
wait = WebDriverWait(driver, 10)
action = ActionChains(driver)
driver.implicitly_wait(5)


def test_pick_business():
    website_url = 'https://buyme.co.il/search?budget=3&category=16&region=11'
    wait.until(ec.url_to_be(website_url))
    assert driver.current_url == website_url
    cards = driver.find_elements(By.XPATH, value='//span[@class="name bm-subtitle-1"]')
    for card in cards:
        if card.text == "בית תאילנדי":
            card.click()
            break

    driver.find_element(By.XPATH, value='//input[@placeholder="הכנס סכום"]').send_keys('250')
    driver.find_element(By.XPATH, value='//button[@type="submit"]').submit()
    driver.close()


test_pick_business()
# class Constants():
#     class PickBusiness(BasePage):
#
#         def __init__(self, driver):
#             BasePage.__init__(self, driver)
#
#         def test_pick_business(self):

