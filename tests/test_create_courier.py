import requests
import pytest
import allure
from urls import BASE_URL
from datasets import *


class TestCreateCourier:

    @allure.title('Создание нового курьера')
    def test_create_new_courier_success(self, create_courier, courier_login, delete_courier):

        response = create_courier["response"]
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        courier_id = courier_login["courier_id"]
        delete_courier(courier_id)

    @allure.title('Создание курьера с таким же логином невозможно')
    def test_create_existing_courier_fails(self, create_courier, courier_login, delete_courier):

        payload = new_courier_credentials
        response = requests.post(f'{BASE_URL}/courier', data=payload)
        assert response.status_code == 409
        assert "Этот логин уже используется" in response.json()["message"]
        courier_id = courier_login["courier_id"]
        delete_courier(courier_id)

    @allure.title('Невозможно создать курьера без обязательных полей')
    @pytest.mark.parametrize('empty_field', empty_required_field)
    def test_create_courier_with_empty_field_fails(self, empty_field):

        payload = empty_field
        response = requests.post(f'{BASE_URL}/courier', data=payload)
        assert response.status_code == 400
        assert "Недостаточно данных" in response.json()["message"]
