
from selenium.webdriver.common.by import By
from base_page import BasePage
from scripts import driver


class Registration(BasePage):

    def __init__(self):
        BasePage.__init__(self, driver)

    def click_login(self):
        self.click_element(By.XPATH, "//span[@tuafontsizes='14']")

    # def click_registration(self):
    #     self.click_element(By.CSS_SELECTOR, 'span[class=text-link theme]')







