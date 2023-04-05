from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from unittest import TestCase
from registration_test import Registration
from selenium.webdriver.chrome.options import Options
import json
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

    def test_1_registration(self):
        self.registration.test_registration()


    def tearDown(self) -> None:
        self.driver.quit()
