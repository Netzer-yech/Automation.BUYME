import time

from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.by import By
from base_page import BasePage

class Constants():
    LOG_IN_BUTTON_TYPE = By.XPATH
    LOG_IN_BUTTON_VALUE = "//span[@tuafontsizes='14']"
    ENTER_BUTTON_TYPE = By.CSS_SELECTOR
    ENTER_BUTTON_VALUE = 'h1[class=bm-h1]'
    REGISTER_BUTTON_TYPE = By.TAG_NAME
    REGISTER_BUTTON_VALUE = 'span'
class Registration(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def test_registration(self):
        self.click_element(Constants.LOG_IN_BUTTON_TYPE, Constants.LOG_IN_BUTTON_VALUE)
        self.click_element_below(Constants.REGISTER_BUTTON_TYPE, Constants.REGISTER_BUTTON_VALUE,
                                 Constants.ENTER_BUTTON_TYPE, Constants.ENTER_BUTTON_VALUE)








