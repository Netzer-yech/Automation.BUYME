from selenium.webdriver.support.relative_locator import locate_with

class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator_type, locator_value):
        self.driver.find_element(locator_type, value=locator_value).click()

    def send_text(self, locator_type, locator_value, text):
        self.driver.find_element(locator_type, value=locator_value).send_keys(text)

    def find_and_return_web_elm(self, locator_type, locator_value):
        return self.driver.find_element(locator_type, value=locator_value)

    def find_elements(self, locator_type, locator_value):
        self.driver.find_elements(locator_type, value=locator_value)

    def click_element_below(self, locator_type, locator_value, relative_type, relative_value):
        self.driver.find_element(locate_with(
            locator_type, locator_value).below(self.find_and_return_web_elm(relative_type, relative_value))).click()



