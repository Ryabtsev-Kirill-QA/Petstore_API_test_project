import allure
import pytest
import requests
import jsonschema
from tests.pet_add import params_add_pet as prm
from framework import assertion, error_msg
from framework.helpers import load_schema
from framework.attach import add_logs_request


@allure.story('Add pet')
class TestAddPet:
    @allure.description(
        """
        Тест POST-запроса на добавление питомца с вызовом 200 ответа
        """
    )
    @allure.title("POST/pet")
    @allure.severity('critical')
    @pytest.mark.parametrize("request_body, status_code", prm.add_pet_positive_post)
    def test_add_pet_positive_post(self, base_url, request_body, headers, status_code):
        schema = load_schema('created_pet.json')

        response = requests.post(f'{base_url}/pet', json=request_body, headers=headers)

        assertion.assertIsNotNone(response, error_msg.ResponceExists)
        assertion.assertStatusCode(response, status_code)
        jsonschema.validate(response.json(), schema)
        add_logs_request(response)


    @allure.description(
        """
        Тест POST-запроса на добавление питомца с вызовом 405 ответа
        """
    )
    @allure.title("POST/pet")
    @allure.severity('critical')
    @allure.tag('negative')
    def test_add_pet_negative_post(self, base_url, headers):

        response = requests.post(f'{base_url}/pet', headers=headers)

        assertion.assertIsNotNone(response, error_msg.ResponceExists)
        assertion.assertStatusCode(response, 405)
        add_logs_request(response)
