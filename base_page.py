from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
import logging
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
logger = logging.getLogger()
logger.setLevel(logging.ERROR)
logging.basicConfig(
                    filename='buy_me.log',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.ERROR,
                    force='True')

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator_type, locator_value):
        try:
            self.driver.find_element(locator_type, value=locator_value).click()
        except Exception as exception:
            logger.error(str(exception))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def send_text(self, locator_type, locator_value, text):
        try:
            self.driver.find_element(locator_type, value=locator_value).send_keys(text)
        except Exception as exception:
            logger.error(str(exception))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def find_elm_and_submit(self, locator_type, locator_value):
        try:
            self.find_web_elm(locator_type, locator_value).submit()
        except Exception as exception:
            logger.error(str(exception))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    def find_web_elm(self, locator_type, locator_value):
        try:
            element = self.driver.find_element(locator_type, value=locator_value)
            return element
        except Exception as exception:
            logger.error(str(exception))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


    def find_and_return_web_elm_text(self, locator_type, locator_value):
        try:
            element = self.driver.find_element(locator_type, value=locator_value)
            return element.text
        except Exception as exception:
            logger.error(str(exception))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def find_elements(self, locator_type, locator_value):
        try:
            return self.driver.find_elements(locator_type, value=locator_value)
        except Exception as exception:
            logger.error(str(exception))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_element_below(self, locator_type, locator_value, relative_type, relative_value):
        try:
            self.driver.find_element(locate_with(locator_type, locator_value).below(
                self.find_web_elm(relative_type, relative_value))).click()
        except Exception as exception:
            logger.error(str(exception))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def get_current_url(self):
        try:
            return self.driver.current_url
        except Exception as exception:
            logger.error(str(exception))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def wait_for_url(self, url):
        try:
            wait(self.driver, 10).until(ec.url_to_be(url))
        except Exception as exception:
            logger.error(str(exception))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def go_to_url(self, url):
        try:
            self.driver.get(url)
        except Exception as exception:
            logger.error(str(exception))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def scroll_down_and_take_screenshot(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
