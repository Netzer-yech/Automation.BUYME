from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import NoSuchElementException
import logging
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# time_out = 10


logger = logging.getLogger()
logger.setLevel(logging.ERROR)
logging.basicConfig(
                    filename='C:\\Users\\netze\\PycharmProjects\\Automation.BUYME\\logfile.log',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.ERROR)
class BasePage():

    def __init__(self, driver):
        self.driver = driver


    def click_element(self, locator_type, locator_value):
        try:
            self.driver.find_element(locator_type, value=locator_value).click()
        except NoSuchElementException as exception:
            logger.exception(str(exception))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def send_text(self, locator_type, locator_value, text):
        try:
            self.driver.find_element(locator_type, value=locator_value).send_keys(text)
        except NoSuchElementException as exception:
            logger.exception(str(exception))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def find_and_return_web_elm(self, locator_type, locator_value):
        try:
            return self.driver.find_element(locator_type, value=locator_value)
        except NoSuchElementException as exception:
            logger.exception(str(exception))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


    def find_and_return_web_elm_text(self, locator_type, locator_value):
        try:
            return self.driver.find_element(locator_type, value=locator_value).text
        except NoSuchElementException as exception:
            logger.exception(str(exception))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def find_elements(self, locator_type, locator_value):
        try:
            self.driver.find_elements(locator_type, value=locator_value)
        except NoSuchElementException as exception:
            logger.exception(str(exception))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_element_below(self, locator_type, locator_value, relative_type, relative_value):
        try:
            self.driver.find_element(locate_with(locator_type, locator_value).below(
                self.find_and_return_web_elm(relative_type, relative_value))).click()
        except NoSuchElementException as exception:
            logger.exception(str(exception))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

