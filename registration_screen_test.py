import time

from selenium.webdriver.common.by import By
from base_page import BasePage
class Constants():
    LOCATOR_XPATH = By.XPATH
    LOG_IN_BUTTON_VALUE = "//span[@tuafontsizes='14']"
    ENTER_BUTTON_TYPE = By.CSS_SELECTOR
    ENTER_BUTTON_VALUE = 'h1[class=bm-h1]'
    REGISTER_BUTTON_TYPE = By.TAG_NAME
    REGISTER_BUTTON_VALUE = 'span'
    FIRST_NAME_TEXT_AREA_VALUE = "//input[@placeholder='שם פרטי']"
    FIRST_NAME_TEXT_AREA_TYPE = By.XPATH
    MAIL_LOCATOR_VALUE = "//input[@placeholder='מייל']"
    MAIL_TEXT = 'netzer.yech@gmail.com'
    PASS_LOCATOR_VALUE = "//input[@placeholder='סיסמה']"
    VARIFAY_PASS_VALUE = "//input[@placeholder='אימות סיסמה']"
    PASS_TEXT = 'Bmrhjzetk91'
    RADIO_BUTTON_VALUE = "//span[@class='circle']"
    SUBMIT_VALUE = "//button[@type='submit']"
class Registration(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def test_registration(self):

        self.click_element(Constants.LOCATOR_XPATH, Constants.LOG_IN_BUTTON_VALUE)
        self.click_element_below(Constants.REGISTER_BUTTON_TYPE, Constants.REGISTER_BUTTON_VALUE,
                                 Constants.ENTER_BUTTON_TYPE, Constants.ENTER_BUTTON_VALUE)
        self.send_text(Constants.LOCATOR_XPATH, Constants.FIRST_NAME_TEXT_AREA_VALUE, 'netzer')
        text_box = self.find_web_elm(By.XPATH, Constants.FIRST_NAME_TEXT_AREA_VALUE).get_attribute('value')
        assert text_box == 'netzer'
        self.send_text(Constants.LOCATOR_XPATH, Constants.MAIL_LOCATOR_VALUE, Constants.MAIL_TEXT)
        self.send_text(Constants.LOCATOR_XPATH, Constants.PASS_LOCATOR_VALUE, Constants.PASS_TEXT)
        self.send_text(Constants.LOCATOR_XPATH, Constants.VARIFAY_PASS_VALUE, Constants.PASS_TEXT)
        self.click_element(Constants.LOCATOR_XPATH, Constants.RADIO_BUTTON_VALUE)
        self.click_element(Constants.LOCATOR_XPATH, Constants.SUBMIT_VALUE)


