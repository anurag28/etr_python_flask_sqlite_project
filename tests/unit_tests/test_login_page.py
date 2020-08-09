from selenium import webdriver


def test_setup():
    global driver
    driver = webdriver.Chrome(
        executable_path="/Users/anuraggarg/Desktop/ETRVersion2/ETRVersion2/resources/webdrivers/chromedriver")


def test_01_launch():
    driver.get('http://127.0.0.1:5000/login')
    assert driver.title == 'ETR'

def test_02_email_field_is_displayed():
    assert driver.find_element_by_id('email').is_displayed()

def test_03_password_field_is_displayed():
    assert driver.find_element_by_id('password').is_displayed()

def test_04_login_button_is_displayed():
    assert driver.find_element_by_id('submit').is_enabled() and driver.find_element_by_id('submit').is_enabled()

def test_02_login():
    driver.find_element_by_xpath(".//a[text()='Login']").click()
    driver.find_element_by_id('email').send_keys('anuraggarg2893@gmail.com')
    driver.find_element_by_id('password').send_keys('anu')
    driver.find_element_by_id('submit').click()
    assert driver.find_element_by_xpath(".//a[text()='Logout']")


def test_teardown():
    driver.close()