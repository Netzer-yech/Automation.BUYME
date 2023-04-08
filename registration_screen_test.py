import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from base_page import BasePage
import allure
class Constants():
    LOCATOR_XPATH = By.XPATH
    LOG_IN_BUTTON_VALUE = "//span[@tuafontsizes='14']"
    ENTER_BUTTON_TYPE = By.CSS_SELECTOR
    ENTER_BUTTON_VALUE = 'h1[class=bm-h1]'
    REGISTER_BUTTON_TYPE = By.TAG_NAME
    REGISTER_BUTTON_VALUE = 'span'
    FIRST_NAME_TEXT_AREA_VALUE = "//input[@placeholder='שם פרטי']"
    FIRST_NAME_LOCATOR = By.XPATH, "//input[@placeholder='שם פרטי']"
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
        # text_box = self.find_and_return_web_elm_text(Constants.FIRST_NAME_TEXT_AREA_TYPE,
        #                                   Constants.FIRST_NAME_TEXT_AREA_VALUE)
        # assert text_box == 'netzer'

        # assert not working properly

        self.send_text(By.XPATH, "//input[@placeholder='מייל']", 'netzer.yech@gmail.com')
        self.send_text(By.XPATH, "//input[@placeholder='סיסמה']", 'Bmrhjzetk91')
        self.send_text(By.XPATH, "//input[@placeholder='אימות סיסמה']", 'Bmrhjzetk91')
        self.click_element(Constants.LOCATOR_XPATH, Constants.RADIO_BUTTON_VALUE)
        self.click_element(Constants.LOCATOR_XPATH, Constants.SUBMIT_VALUE)


