import pytest
import requests


@pytest.fixture
def base_url():
    return 'https://petstore.swagger.io/v2'


@pytest.fixture
def headers():
    headers = \
        {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
    return headers


@pytest.fixture
def add_pet_and_get_id(base_url, headers):
    response = requests.post(f'{base_url}/pet', json={"name": "Test_dog"}, headers=headers)
    pet_id = response.json()["id"]
    return pet_id
