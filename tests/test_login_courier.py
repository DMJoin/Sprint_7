import requests
import pytest
import allure
from datasets import *
from urls import BASE_URL

class TestLoginCourier:

    @allure.title('Успешная авторизация курьера')
    def test_login_courier_success(self, create_courier, delete_courier, get_courier_id):

        payload = auth_credentials 
        response = requests.post(f'{BASE_URL}/courier/login', data=payload)
        assert response.status_code == 200
        assert "id" in response.json()
        delete_courier(get_courier_id)


    @allure.title('Тест авторизации несуществующего курьера')
    def test_authorization_non_existent_courier(self):

        payload = not_exist_courier_credentials
        response = requests.post(f'{BASE_URL}/courier/login', data=payload)
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json()["message"]

    @allure.title('Тест авторизации с неверным паролем')
    def test_authorization_wrong_password_error(self, create_courier, delete_courier, get_courier_id):

        payload = incorrect_auth_credentials
        response = requests.post(f'{BASE_URL}/courier/login', data=payload)
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json()["message"]  
        delete_courier(get_courier_id)


    @allure.title('Проверка ошибки авторизации при отсутствии обязательных полей')
    @pytest.mark.parametrize('empty_params_for_login', empty_authorization_fields)
    def test_login_without_required_field_error(self, create_courier, delete_courier, empty_params_for_login, get_courier_id):

        payload = empty_params_for_login
        response = requests.post(f'{BASE_URL}/courier/login', data=payload)
        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.json()["message"]     
        delete_courier(get_courier_id)