import pytest
import requests
from pprint import pprint

BASE_URL = 'https://restful-booker.herokuapp.com/booking'
AUTH_URL = 'https://restful-booker.herokuapp.com/auth'
STATUS_OK = 200


# Получить все заказы, проверить на статус и наличие заголовка
def test_get_all_booking():
    response = requests.get(BASE_URL)
    assert response.status_code == STATUS_OK
    assert 'Connection' in response.headers, 'There is no expected key'


# Создать заказ и проверить по полю 'firstname'
def test_create_booking():
    payload = {
        "firstname": "James",
        "lastname": "Smith",
        "totalprice": 122,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(BASE_URL, json=payload)
    # pprint(response.json())
    assert response.status_code == STATUS_OK
    id = response.json()['bookingid']
    get_response = requests.get(f'{BASE_URL}/{id}')
    assert get_response.json()['firstname'] == 'James'


# Создать заказ и проверить по полю 'firstname' c фикстурой
# Фикстура для получения 'booking_id'
@pytest.fixture(scope='function')
def booking_id():
    payload = {
        "firstname": "Joe",
        "lastname": "Smith",
        "totalprice": 144,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(BASE_URL, json=payload)
    booking_id = response.json()['bookingid']
    yield booking_id


# Проверка по полю 'firstname', 'booking_id' получаем из фикстуры
def test_create_booking_with_fixture(booking_id):
    response = requests.get(f'{BASE_URL}/{booking_id}')
    assert response.json()['firstname'] == 'Joe'


# Фикстура для получения токена
@pytest.fixture(scope='function')
def token():
    paylod = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(AUTH_URL, json=paylod)
    response_data = response.json()
    token = response_data['token']
    assert response.status_code == STATUS_OK
    yield token


def test_delete_new_booking(booking_id, token):
    headers = {'Cookie': f'token={token}'}
    response = requests.delete(f'{BASE_URL}/{booking_id}', headers=headers)
    assert response.status_code == 201
    get_response = requests.get(f'{BASE_URL}/{booking_id}')
    assert get_response.status_code == 404

# def test_get_booking_with_id():
#     response = requests.get(f'{BASE_URL}/1')
#     response_data = response.json()
#     expected_keys = ['firstname', 'lastname', 'depositpaid', 'totalprice', 'bookingdates']
#
#     print(response.json())
# assert response.status_code == STATUS_OK
# for key in expected_keys:
#     assert key in response_data.keys()
# assert response_data['firstname'] == 'Jim'
