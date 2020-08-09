from selenium import webdriver


def test_setup():
    global driver
    driver = webdriver.Chrome(
        executable_path="/Users/anuraggarg/Desktop/ETRVersion2/ETRVersion2/resources/webdrivers/chromedriver")

def test_01_launch():
    driver.get('http://127.0.0.1:5000/')
    assert driver.title == 'ETR'

def test_02_verify_home_navbar_links_before_login():
    assert driver.find_element_by_xpath(".//a[text()='Home']").is_displayed()


def test_03_verify_login_navbar_links_before_login():
    assert driver.find_element_by_xpath(".//a[text()='Login']").is_displayed()

def test_04_verify_about_navbar_links_before_login():
    assert driver.find_element_by_xpath(".//a[text()='About']").is_displayed()

def test_05_verify_register_navbar_links_before_login():
    assert driver.find_element_by_xpath(".//a[text()='Register']").is_displayed()


def test_teardown():
    driver.close()


