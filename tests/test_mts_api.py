import allure
import requests


URL = "https://shop.mts.ru/apigw/api/v1/search/hits"

HEADERS = {
    'accept': 'application/json',
    'accept-language': 'ru',
    'authorization-jwt': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJ3ZWIiLCJqdGkiOiI2MWNmNjJjNTExMDc5NzE2NWY0MmQ4ZWRjMDZlYzc0NDM5MWFlZmZiMDM1MjFiNmI3N2Y5ODNjMTVkZGM4ZDNkNmVkNGUwZWVjYzRiMGUxZiIsImlhdCI6MTc1Njk5ODk0MS43NTc3NDYsIm5iZiI6MTc1Njk5ODk0MS43NTc3NDgsImV4cCI6MTc1NzAzNDk0MS42MzEwNzgsInN1YiI6Ijg1MzM4ZTkyLWQ2NDYtNGM0My1iY2Q4LWI5MDhiZjM1NGMyNiIsInNjb3BlcyI6W10sImV4dGVybmFsSWQiOiJlM2EzNTI2MC0xNTVmLTExZWItODllZi03YjhkMjVhYTQxNGIiLCJzb3VyY2UiOiJ3ZWJzc28iLCJwaG9uZSI6Ijc5OTIyMjcwMjUwIiwicm9sZXMiOlsiUk9MRV9VU0VSIl0sImNhc2hiYWNrU3RhdHVzIjp7InByZW1pdW1TdGF0dXMiOiJOT19QUkVNSVVNIiwicmVnaXN0ZXJlZCI6dHJ1ZSwiY3JlYXRlZEF0IjoiMjAyNS0wOC0yOFQxNDozODoxMSswMzowMCIsInVwZGF0ZWRBdCI6IjIwMjUtMDktMDRUMTg6MTU6NDErMDM6MDAifX0.HfDcWk_N438uZ_wajJkSoRFAufp4k020Uagad54MCGp1-3FTgbfrQSzMfPxv8UWsk0_hhCYw8y3bmez-6hd6iAVHWUOW6qtc3QaEKRU4yj6zUK0-LzffNUV34iu00O0p1AwyIpYtPdzRVzQocudzMZ17vkrqJKKiz6JUStcQ6IGQxEzdJTBkNSDGNhgmfasf3aXZeSZFlNBaagD_Acf4FoLn3yFDw5rx56JZ738zdirpY-qwfkmRPW6RFZJLSr47HKPPdStXzsui5MHRsHwbcuF4iQ9aA3HS-VC3t-zKDDF2_ADzz2uPljp3ns8cva4WvWZ3gK3KNVGz_X5chjIVkA'
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
