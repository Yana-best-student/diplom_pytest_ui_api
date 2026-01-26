import allure
import requests
import os
from dotenv import load_dotenv

load_dotenv()


URL = os.getenv("API_URL")

HEADERS = {
    'accept': 'application/json',
    'accept-language': 'ru',
    'authorization-jwt': os.getenv("API_TOKEN")
    }


@allure.epic("MTC")
@allure.severity("critical")
@allure.suite("Тесты на работу интернет-магазина МТС")
@allure.story("Поиск товара в магазине")
@allure.title("Поиск товара на кириллице в интернет магазине МТС")
@allure.description(
    "Тест проверяет работу строки поиска товара,"
    " возможность найти товар с названием на кириллице"
)
def test_get_search_list_rus():
    """
    Поиск товара на кириллице.
    :params:передаем список в формате ключ:значение.
    st-наименование товара на кириллице.
    headers: заголовкив формате ключ-значение
    """
    params = {
        'st': 'Смартфон',
        'project': 'shop',
        'platform': 'web'
    }

    with allure.step("Отправить запрос на поиск товара"):
        response = requests.get(URL, headers=HEADERS, params=params)
    with allure.step("Проверить статус ответа"):
        assert response.status_code == 200
        allure.attach(str(response.status_code), name="HTTP Status Code",
                      attachment_type=allure.attachment_type.TEXT)
    with allure.step("Проверить, что ответ содержит данные"):
        assert len(response.json()) > 0
        allure.attach(response.text, name="Response Body",
                      attachment_type=allure.attachment_type.JSON)


@allure.epic("MTC")
@allure.severity("critical")
@allure.suite("Тесты на работу интернет-магазина МТС")
@allure.story("Поиск товара в магазине")
@allure.title(
    "Поиск товара на латинице в интернет магазине МТС")
@allure.description(
    "Тест проверяет работу строки поиска товара,"
    " возможность найти товар с названием на латинице"
)
def test_get_search_list_eng():
    """
    Поиск товара на латинице .
    :params:передаем список в формате ключ:значение.
    st-наименование товара на латинице.
    """
    params = {
        'st': 'iphone',
        'project': 'shop',
        'platform': 'web'
    }

    with allure.step("Отправить запрос на поиск товара"):
        response = requests.get(URL, headers=HEADERS, params=params)
    with allure.step("Проверить статус ответа"):
        assert response.status_code == 200
        allure.attach(str(response.status_code), name="HTTP Status Code",
                      attachment_type=allure.attachment_type.TEXT)
    with allure.step("Проверить, что ответ содержит данные"):
        assert len(response.json()) > 0
        allure.attach(response.text, name="Response Body",
                      attachment_type=allure.attachment_type.JSON)


@allure.epic("MTC")
@allure.severity("critical")
@allure.suite("Тесты на работу интернет-магазина МТС")
@allure.story("Поиск товара в магазине")
@allure.title("Поиск товара на латинице с неверным методом в запросе")
@allure.description(
    "Тест проверяет работу строки поиска товара,"
    " возможность найти товар с названием"
    " на латинице с неверным методом в запросе"
)
def test_put_search_product_method():
    """
    Поиск товара на латинице метод указываем не верный put вместо get.
    :params:передаем список в формате ключ:значение.
    st-наименование товара на латинице.
    """
    params = {
        'st': 'iphone',
        'project': 'shop',
        'platform': 'web'
    }
    with allure.step("Отправить запрос на поиск товара"):
        response = requests.put(URL, headers=HEADERS, params=params)
    with allure.step("Проверить статус ответа"):
        assert response.status_code == 405
        allure.attach(str(response.status_code), name="HTTP Status Code",
                      attachment_type=allure.attachment_type.TEXT)


@allure.epic("MTC")
@allure.severity("critical")
@allure.suite("Тесты на работу интернет-магазина МТС")
@allure.story("Поиск товара в магазине")
@allure.title(
    "Поиск товара со спецсимволами в названии "
    "в интернет магазине МТС")
@allure.description("Тест проверяет работу строки поиска"
                    "товара, возможность найти товар"
                    " с несуществующим названием")
def test_get_search_invalid_query():
    """
    Поиск товара со спецсимволами в названии.
    :params:передаем список в формате ключ:значение.
    st-в наименование товара спецсимволы.
    """
    params = {
        'st': '$@!#^%',
        'project': 'shop',
        'platform': 'web'
    }
    with allure.step("Отправить запрос на поиск товара"):
        response = requests.get(URL, headers=HEADERS, params=params)
    with allure.step("Проверить статус ответа"):
        assert response.status_code == 200
        allure.attach(str(response.status_code), name="HTTP Status Code",
                      attachment_type=allure.attachment_type.TEXT)
    with allure.step("Проверить, что ответ содержит данные"):
        assert len(response.json()) > 0
        allure.attach(response.text, name="Response Body",
                      attachment_type=allure.attachment_type.JSON)


@allure.epic("MTC")
@allure.severity("critical")
@allure.suite("Тесты на работу интернет-магазина МТС")
@allure.story("Поиск товара в магазине")
@allure.title("Поиск товара без параметров в названии в интернет магазине МТС")
@allure.description("Тест проверяет работу строки"
                    " поиска товара на возможность найти товар без названия")
def test_get_search_not_params():
    """
    Поиск товара без названия.
    :params:оставляем без заполнения.
    """
    params = {}

    with allure.step("Отправить запрос на поиск товара"):
        response = requests.get(URL, headers=HEADERS, params=params)
    with allure.step("Проверить статус ответа"):
        assert response.status_code == 200
        allure.attach(str(response.status_code), name="HTTP Status Code",
                      attachment_type=allure.attachment_type.TEXT)
    with allure.step("Проверить, что ответ содержит данные"):
        assert len(response.json()) > 0
        allure.attach(response.text, name="Response Body",
                      attachment_type=allure.attachment_type.JSON)
