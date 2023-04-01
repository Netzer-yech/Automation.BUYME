from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from unittest import TestCase

class TestBuyMeWebsite(TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service("C:\\automation course\\chromedriver.exe"))
        self.driver.get('https://buyme.co.il/')
        self.driver.implicitly_wait(3)
