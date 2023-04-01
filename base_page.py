from selenium.webdriver.chrome.service import Service
from selenium import webdriver

driver = webdriver.Chrome(service=Service("C:\\automation course\\chromedriver.exe"))

class BasePage():

    def __init__(self):
        self.driver = driver

    def click_element(self, locator_type, locator_value):
        self.driver.find_element(locator_type, locator_value).click()

    def send_text(self, locator_type, locator_value):
        self.driver.find_element(locator_type, locator_value).send_keys()