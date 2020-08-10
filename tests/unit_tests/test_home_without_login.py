from selenium import webdriver
import requests


def test_setup():
    global driver
    driver = webdriver.Chrome(
        executable_path="/Users/anuraggarg/Desktop/ETRVersion2/ETRVersion2/resources/webdrivers/chromedriver")

def test_00_verify_homepage_endpoint_response_status_code():
    response = requests.get('http://127.0.0.1:5000')
    assert str(response.status_code) == '200'

def test_01_verify_header_on_home_page():
    response = requests.get('http://127.0.0.1:5000')
    response_body = str(response.content)
    assert 'Home' in response_body and 'Login' in response_body and \
           'Register' in response_body and 'About' in response_body


def test_02_launch():
    driver.get('http://127.0.0.1:5000/')
    assert driver.title == 'ETR'

def test_03_verify_home_navbar_links_before_login():
    assert driver.find_element_by_xpath(".//a[text()='Home']").is_displayed()


def test_04_verify_login_navbar_links_before_login():
    assert driver.find_element_by_xpath(".//a[text()='Login']").is_displayed()

def test_05_verify_about_navbar_links_before_login():
    assert driver.find_element_by_xpath(".//a[text()='About']").is_displayed()

def test_06_verify_register_navbar_links_before_login():
    assert driver.find_element_by_xpath(".//a[text()='Register']").is_displayed()


def test_teardown():
    driver.close()


