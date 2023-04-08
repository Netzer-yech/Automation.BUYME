from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from base_page import BasePage
import allure
class Constants():
    LOG_IN_BUTTON_TYPE = By.XPATH
    LOG_IN_BUTTON_VALUE = "//span[@tuafontsizes='14']"
    ENTER_BUTTON_TYPE = By.CSS_SELECTOR
    ENTER_BUTTON_VALUE = 'h1[class=bm-h1]'
    REGISTER_BUTTON_TYPE = By.TAG_NAME
    REGISTER_BUTTON_VALUE = 'span'
    FIRST_NAME_TEXT_AREA_TYPE = By.XPATH
    FIRST_NAME_TEXT_AREA_VALUE = "//input[@placeholder='שם פרטי']"
    FIRST_NAME_LOCATOR = By.XPATH, "//input[@placeholder='שם פרטי']"
    RADIO_BUTTON_TYPE = By.XPATH
    RADIO_BUTTON_VALUE = "//span[@class='circle']"
    SUBMIT_TYPE = By.XPATH
    SUBMIT_VALUE = "//button[@type='submit']"
class Registration(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def test_registration(self):

        self.click_element(Constants.LOG_IN_BUTTON_TYPE, Constants.LOG_IN_BUTTON_VALUE)
        self.click_element_below(Constants.REGISTER_BUTTON_TYPE, Constants.REGISTER_BUTTON_VALUE,
                                 Constants.ENTER_BUTTON_TYPE, Constants.ENTER_BUTTON_VALUE)
        self.send_text(Constants.FIRST_NAME_TEXT_AREA_TYPE, Constants.FIRST_NAME_TEXT_AREA_VALUE, 'netzer')
        first_name_text_box = self.wait_for_text_and_find_elm(10, Constants.FIRST_NAME_LOCATOR, 'netzer')
        assert first_name_text_box.text == 'netzer'

        self.send_text(By.XPATH, "//input[@placeholder='מייל']", 'netzer.yech@gmail.com')
        self.send_text(By.XPATH, "//input[@placeholder='סיסמה']", 'Bmrhjzetk91')
        self.send_text(By.XPATH, "//input[@placeholder='אימות סיסמה']", 'Bmrhjzetk91')
        self.click_element(Constants.RADIO_BUTTON_TYPE, Constants.RADIO_BUTTON_VALUE)
        self.click_element(Constants.SUBMIT_TYPE, Constants.SUBMIT_VALUE)


