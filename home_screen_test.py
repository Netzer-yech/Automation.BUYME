from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.support.select import Select


class Constants():
    DROP_DOWNS_LOCATOR = By.TAG_NAME, 'select'


class HomeScreen(BasePage):

    def __init__(self, driver):
            BasePage.__init__(self, driver)

    def test_home_screen(self):
        drop_downs = Select(self.find_elements(Constants.DROP_DOWNS_LOCATOR))
        drop_down_1 = drop_downs[0]
        wait.until(ec.presence_of_element_located(drop_downs.select_by_index(3)))
