import requests
import pytest
import allure
from urls import BASE_URL
from datasets import *
from message import *


class TestCreateCourier:

    @allure.title('Создание нового курьера')
    def test_create_new_courier_success(self, create_courier, delete_courier, get_courier_id):

        response = create_courier["response"]
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        delete_courier(get_courier_id)

    @allure.title('Создание курьера с таким же логином невозможно')
    def test_create_existing_courier_fails(self, create_courier, delete_courier, get_courier_id):

        payload = new_courier_credentials
        response = requests.post(f'{BASE_URL}/courier', data=payload)
        assert response.status_code == 409
        assert ERROR_DUPLICATE_LOGIN in response.json()["message"]
        delete_courier(get_courier_id)

    @allure.title('Невозможно создать курьера без обязательных полей')
    @pytest.mark.parametrize('empty_field', empty_required_field)
    def test_create_courier_with_empty_field_fails(self, empty_field):

        payload = empty_field
        response = requests.post(f'{BASE_URL}/courier', data=payload)
        assert response.status_code == 400
        assert ERROR_INSUFFICIENT_DATA in response.json()["message"]
