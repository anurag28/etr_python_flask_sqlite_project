from selenium import webdriver
import requests


def test_setup():
    global driver
    driver = webdriver.Chrome(
        executable_path="/Users/anuraggarg/Desktop/ETRVersion2/ETRVersion2/resources/webdrivers/chromedriver")

def test_00_verify_register_endpoint_response_code():
    response = requests.get('http://127.0.0.1:5000/register')
    assert str(response.status_code) == '200'


def test_01_launch():
    driver.get('http://127.0.0.1:5000/register')
    assert driver.title == 'ETR'

def test_02_email_field_is_displayed():
    assert driver.find_element_by_id('email').is_displayed()

def test_03_username_field_is_displayed():
    assert driver.find_element_by_id('username').is_displayed()

def test_04_password_field_is_displayed():
    assert driver.find_element_by_id('password').is_displayed()

def test_05_confirm_password_field_is_displayed():
    assert driver.find_element_by_id('pass_confirm').is_displayed()

def test_06_register_button_is_displayed():
    assert driver.find_element_by_id('submit').is_displayed() and driver.find_element_by_id('submit').is_enabled()


def test_teardown():
    driver.close()


