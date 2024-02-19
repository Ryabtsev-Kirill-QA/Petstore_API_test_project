import allure
import requests
from framework import assertion, error_msg
from framework.attach import add_logs_request


@allure.story('Delete pet')
class TestDeletePet:
    @allure.description(
        """
        Тест DELETE-запроса на удаление питомца с вызовом 200 ответа
        """
    )
    @allure.title("DELETE/pet")
    @allure.severity('critical')
    def test_pet_positive_delete(self, base_url, headers, add_pet_and_get_id):
        petId = add_pet_and_get_id

        response = requests.delete(f'{base_url}/pet/{petId}', headers=headers)

        assertion.assertIsNotNone(response, error_msg.ResponceExists)
        assertion.assertStatusCode(response, 200)
        add_logs_request(response)

    @allure.description(
        """
        Тест DELETE-запроса на удаление питомца с вызовом 405 ответа
        """
    )
    @allure.title("DELETE/pet")
    @allure.severity('critical')
    @allure.tag('negative')
    def test_pet_negative_delete(self, base_url, headers):

        response = requests.delete(f'{base_url}/pet/', headers=headers)

        assertion.assertIsNotNone(response, error_msg.ResponceExists)
        assertion.assertStatusCode(response, 405)
        add_logs_request(response)

    @allure.description(
        """
        Тест DELETE-запроса на удаление питомца с вызовом 404 ответа
        """
    )
    @allure.title("DELETE/pet")
    @allure.severity('critical')
    @allure.tag('negative')
    def test_pet_not_found_negative_delete(self, base_url, headers):
        response = requests.delete(f'{base_url}/pet/{0}', headers=headers)

        assertion.assertIsNotNone(response, error_msg.ResponceExists)
        assertion.assertStatusCode(response, 404)
        add_logs_request(response)
