from selenium.webdriver.support.relative_locator import locate_with

class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator_type, locator_value):
        self.driver.find_element(locator_type, locator_value).click()

    def send_text(self, locator_type, locator_value, text):
        self.driver.find_element(locator_type, locator_value).send_keys(text)

    def find_element(self, locator_type, locator_value):
        self.driver.find_element(locator_type, locator_value)

    def find_elements(self, locator_type, locator_value):
        self.driver.find_elements(locator_type, locator_value)



