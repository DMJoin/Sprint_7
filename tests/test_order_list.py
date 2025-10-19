import requests
import allure
from urls import BASE_URL

class TestOrderList:

    @allure.title('Получение списка заказов')
    def test_get_order_list_success(self):
        response = requests.get(f'{BASE_URL}/orders')
        assert response.status_code == 200
        assert "orders" in response.json()
