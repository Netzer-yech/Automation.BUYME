import time
from selenium.webdriver.common.by import By
from base_page import BasePage
class Constants():
    LOCATOR_XPATH = By.XPATH
    LOG_IN_BUTTON_VALUE = "//span[@tuafontsizes='14']"
    SUBMIT_VALUE = "//button[@type='submit']"
    ALERT_VALUE = "//li[@class='parsley-required']"
    ALERT_TEXT = 'כל המתנות מחכות לך! אבל קודם צריך מייל וסיסמה'
class Extras(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
    def test_home_screen_error(self):
        self.click_element(Constants.LOCATOR_XPATH, Constants.LOG_IN_BUTTON_VALUE)
        time.sleep(0.1)
        self.click_element(Constants.LOCATOR_XPATH, Constants.SUBMIT_VALUE)
        time.sleep(0.1)
        alert = self.find_and_return_web_elm_text(Constants.LOCATOR_XPATH, Constants.ALERT_VALUE)
        time.sleep(0.1)
        assert alert == Constants.ALERT_TEXT
    def test_screenshot_buttom_of_page(self):
        self.go_to_url('https://buyme.co.il/')
        time.sleep(1)
        self.scroll_down_and_take_screenshot()
