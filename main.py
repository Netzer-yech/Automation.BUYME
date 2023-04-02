from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from unittest import TestCase
from registration import Registration

class TestBuyMeWebsite(TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service("C:\\automation course\\chromedriver.exe"))
        self.driver.get('https://buyme.co.il/')
        self.driver.implicitly_wait(5)
        self.registration = Registration()

    def test_1_registration(self):
        self.registration.click_login()
        # self.registration.click_registration()


    def tearDown(self) -> None:
        self.driver.quit()

