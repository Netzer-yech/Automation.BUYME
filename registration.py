import time

from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.by import By
from base_page import BasePage

class Registration(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def test_registration(self):
        self.click_element(By.XPATH, "//span[@tuafontsizes='14']")
        enter_button = self.find_element(By.CSS_SELECTOR, 'h1[class=bm-h1]')
        self.driver.find_element(locate_with(By.TAG_NAME, 'span').below(enter_button)).click()
        time.sleep(5)








