from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from unittest import TestCase
from registration import Registration
from selenium.webdriver.chrome.options import Options

class TestBuyMeWebsite(TestCase):

    def setUp(self) -> None:
        self.chrome_option = Options()
        self.chrome_option.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(
            "C:\\automation course\\chromedriver.exe"), options=self.chrome_option)
        self.driver.get('https://buyme.co.il/')
        self.driver.implicitly_wait(5)
        self.registration = Registration(self.driver)

    def test_1_registration(self):
        self.registration.test_registration()

    def tearDown(self) -> None:
        self.driver.quit()

