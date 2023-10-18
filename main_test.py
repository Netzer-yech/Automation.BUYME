from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.chrome.options import Options
import json
from registration_screen_test import Registration
from home_screen_test import HomeScreen
from pick_business_test import PickBusiness
from sender_and_receiver import SenderReceiver
from extras_test import Extras
# Import of relevant modules
class TestBuyMeWebsite(TestCase):                  # using TestCase to organize the tests
    def setUp(self) -> None:                       #  Set up any necessary resources or configurations for the test
        self.chrome_option = Options()
        self.chrome_option.add_argument("--start-maximized")  # using Options class for "start maximized" the browser
        json_file = open('../Automation.BUYME/config.json', 'r')       # open the json file
        data = json.load(json_file)                # loading the json content to the variable "data"
        browser = data['browserType']
        url = data['url']
        if browser == 'chrome' and url == "https://buyme.co.il/":
            self.driver = webdriver.Chrome(service=Service(
                "C:\\automation course\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"), options=self.chrome_option)
            self.driver.get('https://buyme.co.il/')
            json_file.close()
        elif browser == 'edge' and url == "https://buyme.co.il/":
            self.driver = webdriver.Edge(service=Service(
                "C:\\automation course\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"))
            self.driver.get('https://buyme.co.il/')
            json_file.close()                       # reading the json content and define the driver and url for the program
        self.driver.implicitly_wait(5)              # waiting generally for element to appear, for safety
        self.registration = Registration(self.driver)
        self.home_screen = HomeScreen(self.driver)
        self.pick_business = PickBusiness(self.driver)
        self.sender_receiver = SenderReceiver(self.driver)
        self.extras = Extras(self.driver)           # define the objects of the different test using POM
    def test_1_registration(self):
        self.registration.test_registration()
    def test_2_home_screen(self):
        self.home_screen.test_home_screen()
    def test_3_pick_business(self):                  # each function calling the test from his module
        self.pick_business.test_pick_business()
    def test_4_sender_receiver(self):
        self.sender_receiver.test_sender_receiver()
    def test_5_extras(self):
        self.extras.test_home_screen_error()
        self.extras.test_screenshot_buttom_of_page()
    def tearDown(self) -> None:
        self.driver.quit()                           # tearDown for ending the main test