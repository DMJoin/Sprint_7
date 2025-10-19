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
def courier_login():
    login_payload = auth_credentials
    login_response = requests.post(f'{urls.BASE_URL}/courier/login', data=login_payload)
    courier_id = login_response.json().get('id')
    return {
        "response": login_response,
        "courier_id" : courier_id
    }


@pytest.fixture
def delete_courier():
    def _delete(courier_id):
        response = requests.delete(f"{urls.BASE_URL}/courier/{courier_id}")
        return response
    return _delete 