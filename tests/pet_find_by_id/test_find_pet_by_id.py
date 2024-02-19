import allure
import requests
import jsonschema
from framework.helpers import load_schema
from framework import assertion, error_msg
from framework.attach import add_logs_request


@allure.story('Find pet by id')
class TestDeletePet:
    @allure.description(
        """
        Тест GET-запроса на поиск питомца с вызовом 200 ответа
        """
    )
    @allure.title("GET/pet")
    @allure.severity('critical')
    def test_pet_positive_get(self, base_url, headers, add_pet_and_get_id):
        petId = add_pet_and_get_id
        schema = load_schema('get_pet.json')

        response = requests.get(f'{base_url}/pet/{petId}', headers=headers)

        assertion.assertIsNotNone(response, error_msg.ResponceExists)
        assertion.assertStatusCode(response, 200)
        jsonschema.validate(response.json(), schema)
        add_logs_request(response)

    @allure.description(
        """
        Тест GET-запроса на удаление питомца с вызовом 404 ответа
        """
    )
    @allure.title("GET/pet")
    @allure.severity('critical')
    @allure.tag('negative')
    def test_pet_not_found_negative_get(self, base_url, headers):
        response = requests.get(f'{base_url}/pet/{922337203685477580700}', headers=headers)

        assertion.assertIsNotNone(response, error_msg.ResponceExists)
        assertion.assertStatusCode(response, 404)
        add_logs_request(response)
