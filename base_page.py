from selenium.webdriver.support.relative_locator import locate_with

class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator_type, locator_value):
        self.driver.find_element(locator_type, locator_value).click()

    def send_text(self, locator_type, locator_value):
        self.driver.find_element(locator_type, locator_value).send_keys()

    def find_element(self, locator_type, locator_value):
        self.driver.find_element(locator_type, locator_value)

    def find_elements(self, locator_type, locator_value):
        self.driver.find_elements(locator_type, locator_value)

    def click_element_locate_with_below(self, locator_type, locator_value, element_located):
        self.driver.find_element(locate_with(locator_type, locator_value).below(element_located))
