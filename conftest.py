import pytest
import requests


@pytest.fixture()
def obj_id():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post(url='https://api.restful-api.dev/objects', json=payload).json()
    yield response['id']
    requests.delete(f'https://api.restful-api.dev/objects/{response['id']}')


@pytest.fixture(scope='session')
def all_tests():
    print('Start tests all')
    yield
    print(' Finish tests all')