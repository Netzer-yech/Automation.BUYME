import time
from base_page import BasePage
from selenium.webdriver.common.by import By
class Constants:             # constant variable using for easy maintenance of locator and values of elements
    LOCATOR = By.XPATH
    CARD_VALUE = '//span[@class="name bm-subtitle-1"]'
    TEXT_BOX_VALUE = '//input[@placeholder="הכנס סכום"]'
    TEXT_BOX_TEXT = '250'
    SUBMIT_VALUE = '//button[@type="submit"]'
class PickBusiness(BasePage):                   # using inheritance to use all functionality from the BasePage class
    def __init__(self, driver):                 # construct the driver again at child-class for future inheritance
        BasePage.__init__(self, driver)
        # calling parent constructor to initialize the attributes of the parent class with child class

    def test_pick_business(self):
        self.go_to_url('https://buyme.co.il/search?budget=3&category=16&region=11')
        current_url = self.get_current_url()
        website_url = 'https://buyme.co.il/search?budget=3&category=16&region=11'
        self.wait_for_url(website_url)
        assert current_url == website_url  # assert that current url as expected
        cards = self.find_elements(Constants.LOCATOR, Constants.CARD_VALUE)
        for card in cards:                # using for loop to iterate between element with the same attributes
            if card.text == "בית תאילנדי":
                card.click()
                break
        self.send_text(Constants.LOCATOR, Constants.TEXT_BOX_VALUE, Constants.TEXT_BOX_TEXT)
        self.find_elm_and_submit(Constants.LOCATOR, Constants.SUBMIT_VALUE)






