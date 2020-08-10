import requests


def test_01_verify_logout_endpoint():
    response = str(requests.get('http://localhost:5000/logout').status_code)
    assert response == '200'

def test_02_verify_about_endpoint():
    response = str(requests.get('http://localhost:5000/about').status_code)
    assert response == '200'


def test_03_verify_search_endpoint():
    response = str(requests.get('http://localhost:5000/search_movies').status_code)
    assert response == '200'


def test_04_verify_create_post_endpoint():
    response = str(requests.get('http://localhost:5000/add_movie').status_code)
    assert response == '200'


def test_05_verify_particular_post_endpoint():
    response = str(requests.get('http://localhost:5000/4').status_code)
    assert response == '200'


def test_06_verify_other_user_posts_endoint():
    response = str(requests.get('http://localhost:5000/a').status_code)
    assert response == '200'

def test_07_verify_delete_endpoint():
    response = str(requests.post('http://localhost:5000/3/delete').status_code)
    assert response == '200'

def test_08_verify_update_end_point():
    response = str(requests.get('http://localhost:5000/4/update').status_code)
    assert response == '200'


