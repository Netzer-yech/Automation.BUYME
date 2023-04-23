from selenium.webdriver.common.by import By
from base_page import BasePage
import time
class Constants():                     # constant variable using for easy maintenance of locator and values of elements
    LOCATOR = By.XPATH

class HomeScreen(BasePage):             # using inheritance to use all functionality from the BasePage class

    def __init__(self, driver):                  # construct the driver again at child-class for future inheritance
            BasePage.__init__(self, driver)
        # calling parent constructor to initialize the attributes of the parent class with child class


    def test_home_screen(self):
        self.click_element(Constants.LOCATOR, "//span[@title='סכום']")
        self.click_element(Constants.LOCATOR, "//li[@value='3']")
        self.click_element(Constants.LOCATOR, "//span[@title='אזור']")
        self.click_element(Constants.LOCATOR, "//li[@value='11']")
        self.click_element(Constants.LOCATOR, "//span[@title='קטגוריה']")
        self.click_element(Constants.LOCATOR, "//li[@value='391']")
        self.click_element(Constants.LOCATOR, "//a[@rel='nofollow']")

        # time-sleep is the only waiting technic that works in this part of the test (select from dropdowns)