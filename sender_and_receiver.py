import time
from base_page import BasePage
from selenium.webdriver.common.by import By
class Constants():                    # constant variable using for easy maintenance of locator and values of elements
    LOCATOR_XPATH = By.XPATH
    RECEIVER_NAME = 'daniel gotlib'
    RECEIVER_TEXT_AREA = "//input[@maxlength='25']"
    PICTURE = "C:\\automation course\\picture.png"
class SenderReceiver(BasePage):              # using inheritance to use all functionality from the BasePage class
    def __init__(self, driver):              # construct the driver again at child-class for future inheritance
        BasePage.__init__(self, driver)
        # calling parent constructor to initialize the attributes of the parent class with child class
    def test_sender_receiver(self):
        self.go_to_url('https://buyme.co.il/money/370060?price=250')
        self.click_element(Constants.LOCATOR_XPATH, "//div[@gtm='למישהו אחר']")
        self.send_text(Constants.LOCATOR_XPATH, Constants.RECEIVER_TEXT_AREA, Constants.RECEIVER_NAME)
        self.click_element(Constants.LOCATOR_XPATH, '//span[@title="לאיזה אירוע?"]')
        time.sleep(0.1)                      # minimum of time.sleep to help code reaching the element inside dropdown
        self.click_element(Constants.LOCATOR_XPATH, '//li[@value="59"]')
        self.find_textbox_and_clear(Constants.LOCATOR_XPATH, '//textarea[@rows="4"]')
        self.send_text(Constants.LOCATOR_XPATH, '//textarea[@rows="4"]', "באהבה רבה!!!")
        self.send_text(Constants.LOCATOR_XPATH, '//input[@type="file"]', Constants.PICTURE)
        time.sleep(1)                         # minimum of time.sleep to make sure picture is uploaded correctly
        self.find_elm_and_submit(Constants.LOCATOR_XPATH, '//button[@gtm="המשך"]')
        self.click_element(Constants.LOCATOR_XPATH, '//div[@gtm="עכשיו"]')
        svgs = self.find_elements(By.TAG_NAME, 'svg')
        for svg_sms in svgs:                  # using for loop to iterate between element with the same attributes
            if svg_sms.get_attribute('gtm') == 'method-sms':
                time.sleep(0.1)
                svg_sms.click()
                break
        self.send_text(Constants.LOCATOR_XPATH, '//input[@id="sms"]', "0524399521")
        self.send_text(Constants.LOCATOR_XPATH, '//input[@placeholder="שם שולח המתנה"]', "נצר מפתח אוטומציה")
        self.go_to_last_page()
        receiver_name = self.find_web_elm(Constants.LOCATOR_XPATH, Constants.RECEIVER_TEXT_AREA).get_attribute('value')
        assert receiver_name == Constants.RECEIVER_NAME
        # assert receiver name don't changed after going back to last page