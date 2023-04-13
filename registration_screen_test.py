from selenium.webdriver.common.by import By
from base_page import BasePage
class Constants():                    # constant variable using for easy maintenance of locator and values of elements
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
class Registration(BasePage):             # using inheritance to use all functionality from the BasePage class
    def __init__(self, driver):           # construct the driver again at child-class for future inheritance
        BasePage.__init__(self, driver)
        # calling parent constructor to initialize the attributes of the parent class with child class
    def test_registration(self):
        self.click_element(Constants.LOCATOR_XPATH, Constants.LOG_IN_BUTTON_VALUE)
        self.click_element_below(Constants.REGISTER_BUTTON_TYPE, Constants.REGISTER_BUTTON_VALUE,
                                 Constants.ENTER_BUTTON_TYPE, Constants.ENTER_BUTTON_VALUE)
        self.send_text(Constants.LOCATOR_XPATH, Constants.FIRST_NAME_TEXT_AREA_VALUE, 'netzer')
        text_box = self.find_web_elm(By.XPATH, Constants.FIRST_NAME_TEXT_AREA_VALUE).get_attribute('value')
        assert text_box == 'netzer'   # assert that text_box is equal to the actual attribute of 'value'
        self.send_text(Constants.LOCATOR_XPATH, Constants.MAIL_LOCATOR_VALUE, Constants.MAIL_TEXT)
        self.send_text(Constants.LOCATOR_XPATH, Constants.PASS_LOCATOR_VALUE, Constants.PASS_TEXT)
        self.send_text(Constants.LOCATOR_XPATH, Constants.VARIFAY_PASS_VALUE, Constants.PASS_TEXT)
        self.click_element(Constants.LOCATOR_XPATH, Constants.RADIO_BUTTON_VALUE)
        self.click_element(Constants.LOCATOR_XPATH, Constants.SUBMIT_VALUE)

        # using all function from base class for the test flow
