from base_page import BasePage

class Constants():
    class PickBusiness(BasePage):

        def __init__(self, driver):
            BasePage.__init__(self, driver)

        def test_pick_business(self):
