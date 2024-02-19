import allure
import requests
import jsonschema
from framework.helpers import load_schema
from framework import assertion, error_msg
from framework.attach import add_logs_request


@allure.story('Update pet name')
class TestDeletePet:
    @allure.description(
        """
        Тест POST-запроса на изменение имени питомца с вызовом 200 ответа
        """
    )
    @allure.title("POST/pet")
    @allure.severity('critical')
    def test_update_pet_positive_post(self, base_url, headers, add_pet_and_get_id):
        petId = add_pet_and_get_id
        payload = {'name=new_name_of_pet'}
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        schema = load_schema('update_pet.json')

        response = requests.post(f'{base_url}/pet/{petId}', headers=headers, data=payload)
        #check_changes = requests.get(f'{base_url}/pet/{petId}', headers=headers)

        assertion.assertIsNotNone(response, error_msg.ResponceExists)
        assertion.assertStatusCode(response, 200)
        #assert check_changes.json()['name'] == 'new_name_of_pet'
        jsonschema.validate(response.json(), schema)
        add_logs_request(response)
