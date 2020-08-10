from selenium import webdriver


def test_setup():
    global driver
    driver = webdriver.Chrome(
        executable_path="C:/Users/nikun/OneDrive/Desktop/ETR/etr_python_flask_sqlite_project/resources/webdrivers/chromedriver.exe")


def test_01_launch():
    driver.get('http://127.0.0.1:5000/')
    assert driver.title == 'ETR'


def test_login():
    driver.find_element_by_xpath(".//a[text()='Login']").click()
    driver.find_element_by_id('email').send_keys('anuraggarg2893@gmail.com')
    driver.find_element_by_id('password').send_keys('anu')
    driver.find_element_by_id('submit').click()
    assert driver.find_element_by_xpath(".//a[text()='Logout']")


def test_account():
    driver.find_element_by_xpath("/html/body/nav/ul/li[4]/a").click()
    assert driver.find_element_by_id("username").get_attribute('value') in driver.find_element_by_xpath("/html/body/div[1]/div/h1").text


def test_name():
    assert driver.find_element_by_id("name").get_attribute("value") is not None


def test_submit():
    assert driver.find_element_by_id("submit").is_displayed()


def test_teardown():
    driver.close()
