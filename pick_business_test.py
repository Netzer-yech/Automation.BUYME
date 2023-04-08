from base_page import BasePage
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# chrome_option = Options()
# chrome_option.add_argument("--start-maximized")
# driver = webdriver.Chrome(service=Service("C:\\automation course\\chromedriver.exe"), options=chrome_option)
# driver.get('https://buyme.co.il/search?budget=3&category=16&region=11')
# wait = WebDriverWait(driver, 10)
# action = ActionChains(driver)
# driver.implicitly_wait(5)


# def test_pick_business():
#     website_url = 'https://buyme.co.il/search?budget=3&category=16&region=11'
#     wait.until(ec.url_to_be(website_url))
#     assert driver.current_url == website_url
#     cards = driver.find_elements(By.XPATH, value='//span[@class="name bm-subtitle-1"]')
#     for card in cards:
#         if card.text == "בית תאילנדי":
#             card.click()
#             break
#
#     driver.find_element(By.XPATH, value='//input[@placeholder="הכנס סכום"]').send_keys('250')
#     driver.find_element(By.XPATH, value='//button[@type="submit"]').submit()




# page need to write as POM!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Constants():

    LOCATOR = By.XPATH
    CARD_VALUE = '//span[@class="name bm-subtitle-1"]'
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






