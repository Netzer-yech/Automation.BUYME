import time

from base_page import BasePage
from selenium.webdriver.common.by import By
class Constants():

    LOCATOR = By.XPATH
    CARD_VALUE = '//span[@class="name bm-subtitle-"]'
    TEXT_BOX_VALUE = '//input[@placeholder="הכנס סכום"]'
    TEXT_BOX_TEXT = '250'
    SUBMIT_VALUE = '//button[@type="submit"]'

class PickBusiness(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def test_pick_business(self):

        self.go_to_url('https://buyme.co.il/search?budget=3&category=16&region=11')
        # this line should be delete after finish to write the second page "home-screen"
        # program needs to work with one flow

        current_url = self.get_current_url()
        website_url = 'https://buyme.co.il/search?budget=3&category=16&region=11'
        self.wait_for_url(10, website_url)
        assert current_url == website_url
        cards = self.find_elements(Constants.LOCATOR, Constants.CARD_VALUE)
        for card in cards:
            if card.text == "בית תאילנדי":
                card.click()
                break

        self.send_text(Constants.LOCATOR, Constants.TEXT_BOX_VALUE, Constants.TEXT_BOX_TEXT)
        self.find_elm_and_submit(Constants.LOCATOR, Constants.SUBMIT_VALUE)






