import requests
import pytest
import urls
from datasets import *

@pytest.fixture
def create_courier():
    payload = new_courier_credentials
    response = requests.post(f'{urls.BASE_URL}/courier', data=payload)
    return{
        "response" : response
    }

@pytest.fixture
def delete_courier():
    def _delete(courier_id):
        response = requests.delete(f"{urls.BASE_URL}/courier/{courier_id}")
        return response
    return _delete 

@pytest.fixture
def get_courier_id():
    login_payload = new_courier_credentials

    response = requests.post(f'{urls.BASE_URL}/courier/login', data=login_payload)
    if response.status_code == 200:
        return response.json().get('id')
    return None