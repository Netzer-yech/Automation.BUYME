import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pyautogui

chrome_option = Options()
chrome_option.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service("C:\\automation course\\chromedriver.exe"), options=chrome_option)
driver.get('https://buyme.co.il/')
action = ActionChains(driver)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)


# def test_1():
#     driver.find_element(By.XPATH, value="//span[@tuafontsizes='14']").click()
#     my_button = driver.find_element(By.CSS_SELECTOR, value='h1[class=bm-h1]')
#     driver.find_element(locate_with(By.TAG_NAME, 'span').below(my_button)).click()
#     driver.find_element(By.XPATH, value="//input[@placeholder='שם פרטי']").send_keys('netzer')
#     driver.find_element(By.XPATH, value="//input[@placeholder='מייל']").send_keys('netzer.yech@gmail.com')
#     driver.find_element(By.XPATH, value="//input[@placeholder='סיסמה']").send_keys('Bmrhjzetk91')
#     driver.find_element(By.XPATH, value="//input[@placeholder='אימות סיסמה']").send_keys('Bmrhjzetk91')
#     driver.find_element(By.XPATH, value="//span[@class='circle']").click()
#     first_name_text_area = driver.find_element(By.XPATH, value="//input[@placeholder='שם פרטי']").get_attribute('value')
#     first_name = 'netzer'
#     assert first_name == first_name_text_area
#     driver.find_element(By.XPATH, value="//button[@type='submit']").click()
# test_1()
#
#
#
# time.sleep(5)



# time.sleep(10)

# def test_3():
#     website_url = 'https://buyme.co.il/'
#     assert driver.current_url == website_url
#     driver.find_element(By.CSS_SELECTOR, value='div[class=bottom]').click()
#     time.sleep(5)

# driver.find_element(By.XPATH, value="//span[@tuafontsizes='14']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, value="//button[@type='submit']").click()
# alert_text = 'כל המתנות מחכות לך! אבל קודם צריך מייל וסיסמה'
# alerts = driver.find_element(By.XPATH, value="//li[@class='parsley-required']").text
# assert alerts == alert_text
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)


