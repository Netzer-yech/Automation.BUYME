import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

chrome_option = Options()
chrome_option.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service("C:\\automation course\\chromedriver.exe"), options=chrome_option)
driver.get('https://buyme.co.il/')
action = ActionChains(driver)
driver.implicitly_wait(5)


def test_1():
    driver.find_element(By.XPATH, value="//span[@tuafontsizes='14']").click()
    my_button = driver.find_element(By.CSS_SELECTOR, value='h1[class=bm-h1]')
    driver.find_element(locate_with(By.TAG_NAME, 'span').below(my_button)).click()
    driver.find_element(By.XPATH, value="//input[@placeholder='שם פרטי']").send_keys('netzer')
    driver.find_element(By.XPATH, value="//input[@placeholder='מייל']").send_keys('netzer.yech@gmail.com')
    driver.find_element(By.XPATH, value="//input[@placeholder='סיסמה']").send_keys('Bmrhjzetk91')
    driver.find_element(By.XPATH, value="//input[@placeholder='אימות סיסמה']").send_keys('Bmrhjzetk91')
    driver.find_element(By.XPATH, value="//span[@class='circle']").click()
    first_name_text_area = driver.find_element(By.XPATH, value="//input[@placeholder='שם פרטי']")
    action.move_to_element(first_name_text_area).perform()
    first_name = 'netzer'
    print(first_name_text_area.text)
    # assert first_name == first_name_text_area.text
    driver.find_element(By.XPATH, value="//button[@type='submit']").click()

def test_2():
    select = Select(driver.find_element(By.TAG_NAME, value='select'))
    print(select.select_by_index(2).text)

test_2()
time.sleep(7)






