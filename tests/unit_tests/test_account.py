from selenium import webdriver
import requests


def test_setup():
    global driver
    driver = webdriver.Chrome(
        executable_path="/Users/anuraggarg/Desktop/ETRVersion2/ETRVersion2/resources/webdrivers/chromedriver")


def test_00_launch_and_login():
    driver.get('http://127.0.0.1:5000/')
    driver.find_element_by_xpath(".//a[text()='Login']").click()
    driver.find_element_by_id('email').send_keys('anuraggarg2893@gmail.com')
    driver.find_element_by_id('password').send_keys('anu')
    driver.find_element_by_id('submit').click()
    assert driver.find_element_by_xpath(".//a[text()='Logout']")

def test_01_verify_response_code_of_account_endpoint():
    response = requests.get('http://127.0.0.1:5000/account')
    assert str(response.status_code) == '200'

def test_02_verify_correct_ucername_is_displayed():
    driver.find_element_by_xpath(".//a[text()='Account']").click()
    assert driver.find_element_by_id("username").get_attribute('value') in driver.find_element_by_xpath("/html/body/div[1]/div/h1").text


def test_03_verify_correct_name_is_displayed():
    assert driver.find_element_by_id("name").get_attribute("value") is not None


def test_04_verify_update_button_is_displayed():
    assert driver.find_element_by_id("submit").is_displayed()

def test_05_verify_image_link_is_working():
    response = requests.get('http://127.0.0.1:5000/static/profile_pics/anurag.jpg')
    assert str(response.status_code) == '200'

def test_06_verify_email_is_displayed():
    assert driver.find_element_by_id('email').get_attribute('value') is not None

def test_teardown():
    driver.close()
