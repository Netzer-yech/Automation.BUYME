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

class Registration(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def test_registration(self):

        self.click_element(Constants.LOG_IN_BUTTON_TYPE, Constants.LOG_IN_BUTTON_VALUE)
        self.click_element_below(Constants.REGISTER_BUTTON_TYPE, Constants.REGISTER_BUTTON_VALUE,
                                 Constants.ENTER_BUTTON_TYPE, Constants.ENTER_BUTTON_VALUE)
        self.send_text(By.XPATH, Constants.FIRST_NAME_TEXT_AREA_VALUE, 'netzer')
        self.send_text(By.XPATH, "//input[@placeholder='מייל']", 'netzer.yech@gmail.com')
        self.send_text(By.XPATH, "//input[@placeholder='סיסמה']", 'Bmrhjzetk91')
        self.send_text(By.XPATH, "//input[@placeholder='אימות סיסמה']", 'Bmrhjzetk91')
        self.click_element(By.XPATH, "//span[@class='circle']")
        first_name = 'netzer'
        first_name_text_area = self.find_and_return_web_elm_text(
            Constants.FIRST_NAME_TEXT_AREA_TYPE, Constants.FIRST_NAME_TEXT_AREA_VALUE)
        self.click_element(By.XPATH, "//button[@type='submit']")
        # assert first_name_text_area.text == first_name


