from selenium.webdriver.common.by import By
from base_page import BasePage
import time
class Constants():
    LOCATOR = By.XPATH

class HomeScreen(BasePage):

    def __init__(self, driver):
            BasePage.__init__(self, driver)

    def test_home_screen(self):
        self.go_to_url('https://buyme.co.il/')
        self.click_element(Constants.LOCATOR, "//span[@title='סכום']")
        time.sleep(0.1)
        self.click_element(Constants.LOCATOR, "//li[@value='3']")
        time.sleep(0.1)
        self.click_element(Constants.LOCATOR, "//span[@title='אזור']")
        time.sleep(0.1)
        self.click_element(Constants.LOCATOR, "//li[@value='11']")
        time.sleep(0.1)
        self.click_element(Constants.LOCATOR, "//span[@title='קטגוריה']")
        time.sleep(0.1)
        self.click_element(Constants.LOCATOR, "//li[@value='391']")
        time.sleep(0.1)
        self.click_element(Constants.LOCATOR, "//a[@rel='nofollow']")
