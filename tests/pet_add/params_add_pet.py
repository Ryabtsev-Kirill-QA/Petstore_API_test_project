import pytest

add_pet_positive_post = [
    pytest.param(
            {
                "id": 0,
                "category": {
                    "id": 0,
                    "name": "Test_Pet"
                },
                "name": "doggie",
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 0,
                        "name": "Test_Pet"
                    }
                ],
                "status": "available"
        },
        200,
        marks=pytest.mark.positive,
    ),
]

