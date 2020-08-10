from selenium import webdriver


def test_setup():
    global driver
    driver = webdriver.Chrome(
        executable_path="/Users/anuraggarg/Desktop/ETRVersion2/ETRVersion2/resources/webdrivers/chromedriver")


def test_launch_login_moviepage():
    driver.get('http://127.0.0.1:5000/')
    driver.find_element_by_xpath(".//a[text()='Login']").click()
    driver.find_element_by_id('email').send_keys('anuraggarg2893@gmail.com')
    driver.find_element_by_id('password').send_keys('anu')
    driver.find_element_by_id('submit').click()
    driver.get("http://127.0.0.1:5000/add_movie")
    assert driver.find_element_by_xpath('//*[@id="name"]').is_displayed()


def test_add_movie():
    driver.find_element_by_id('name').send_keys('Titanic')
    driver.find_element_by_id('cast').send_keys('Naresh Kanodiya')
    driver.find_element_by_id('genre').send_keys('Romantic')
    driver.find_element_by_id('rating').send_keys('10')
    driver.find_element_by_id('comment').send_keys('Awesome Movie')
    driver.find_element_by_id('submit').click()


def test_teardown():
    driver.close()
