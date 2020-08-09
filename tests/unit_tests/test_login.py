from selenium import webdriver


def test_setup():
    global driver
    driver = webdriver.Chrome(
        executable_path="/Users/anuraggarg/Desktop/ETRVersion2/ETRVersion2/resources/webdrivers/chromedriver")

def test_01_launch():
    driver.get('http://127.0.0.1:5000/')
    assert driver.title == 'ETR'

def test_02_login():
    pass

def test_teardown():
    driver.close()


