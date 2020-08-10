from selenium import webdriver


def test_setup():
    global driver
    driver = webdriver.Chrome(
        executable_path="/Users/anuraggarg/Desktop/ETRVersion2/ETRVersion2/resources/webdrivers/chromedriver")


def test_launch_login():
    driver.get('http://127.0.0.1:5000/')
    driver.find_element_by_xpath(".//a[text()='Login']").click()
    driver.find_element_by_id('email').send_keys('anuraggarg2893@gmail.com')
    driver.find_element_by_id('password').send_keys('anu')
    driver.find_element_by_id('submit').click()
    assert driver.find_element_by_xpath(".//a[text()='Logout']")


def test_name():
    driver.get("http://127.0.0.1:5000/add_movie")
    assert driver.find_element_by_xpath('//*[@id="name"]').is_displayed()


def test_cast():
    assert driver.find_element_by_id("cast").is_displayed()


def test_genre():
    assert driver.find_element_by_id("genre").is_displayed()


def test_rating():
    assert driver.find_element_by_id("rating").is_displayed()


def test_comment():
    assert driver.find_element_by_id("comment").is_displayed()


def test_comment():
    assert driver.find_element_by_id("submit").is_displayed()


def test_teardown():
    driver.close()
