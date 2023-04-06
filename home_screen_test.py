from selenium.webdriver.common.by import By
from base_page import BasePage

class Constants():
    class HomeScreen(BasePage):

        def __init__(self, driver):
            BasePage.__init__(self, driver)

        def test_home_screen(self):
