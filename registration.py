from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.by import By
from base_page import BasePage

class Registration(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def click_login(self):
        self.click_element(By.XPATH, "//span[@tuafontsizes='14']")

    def click_registration(self):
        enter_button = self.find_element(By.CSS_SELECTOR, 'h1[class=bm-h1]')
        self.click_element_locate_with_below(By.TAG_NAME, 'span', enter_button)









