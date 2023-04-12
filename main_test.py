from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.chrome.options import Options
import json
from registration_screen_test import Registration
from home_screen_test import HomeScreen
from pick_business_test import PickBusiness
# from sender_and_receiver import SenderReceiver
from extras_test import Extras

class TestBuyMeWebsite(TestCase):

    def setUp(self) -> None:
        self.chrome_option = Options()
        self.chrome_option.add_argument("--start-maximized")
        json_file = open('config.json', 'r')
        data = json.load(json_file)
        browser = data['browserType']
        url = data['url']
        if browser == 'chrome' and url == "https://buyme.co.il/":
            self.driver = webdriver.Chrome(service=Service(
                "C:\\automation course\\chromedriver.exe"), options=self.chrome_option)
            self.driver.get('https://buyme.co.il/')
            json_file.close()
        elif browser == 'edge' and url == "https://buyme.co.il/":
            self.driver = webdriver.Edge(service=Service("C:\\automation course\\msedgedriver.exe"))
            self.driver.get('https://buyme.co.il/')
            json_file.close()
        self.driver.implicitly_wait(10)
        self.registration = Registration(self.driver)
        self.home_screen = HomeScreen(self.driver)
        self.pick_business = PickBusiness(self.driver)
        self.extras = Extras(self.driver)
    def test_1_registration(self):
        self.registration.test_registration()
    def test_2_home_screen(self):
        self.home_screen.test_home_screen()
    def test_3_pick_business(self):
        self.pick_business.test_pick_business()
    def test_5_extras(self):
        self.extras.test_home_screen_error()
    def tearDown(self) -> None:
        self.driver.quit()

