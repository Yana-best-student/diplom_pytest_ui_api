import allure
from page.UiPage import UiPage
from page.CartPage import CartPage
from page.PayPage import PayPage
from page.DelPage import DelPage
from page.NegativPage import NegativPage
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("МТС")
@allure.story("Поиск товара на латинице")
@allure.title("Поиск товара на латинице в интернет магазине МТС")
@allure.description("Тест проверяет работу строки поиска товара, "
                    "возможность найти товар с названием на латинице")
@allure.severity(allure.severity_level.BLOCKER)
def test_first(browser):
    """
    Поиск товара на латинице .
    :param browser: webdriver - объект драйвера, переданый фикстурой.
    """
    with allure.step("Открытие главной страницы интернет-магазина"):
        auth_page = UiPage(browser)
    with allure.step("Открывает страницу 'shop.mts.ru' в браузере"):
        auth_page.go()
    with allure.step("Передаем значение cookie"):
        auth_page.set_cookie_policy()
    with allure.step("Ввод названия товара на латинице через поисковую строку"):
        auth_page.search('iphone')

    with allure.step("Проверка результата:список товаров не пустой"):
        results = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".card-name.product-card__name-link"))
        )
        assert len(results) > 0, "Список товаров пуст!"
        print("Список товаров не пуст.")


@allure.feature("МТС")
@allure.story("Поиск товара в магазине и добавление его в корзину")
@allure.title("Поиск товара и добавление его в корзину в "
              "интернет магазине МТС")
@allure.description("Тест проверяет возможность добавления "
                    "выбранного товара в корзину,"
                    " работоспособность кнопки купить")
@allure.severity(allure.severity_level.BLOCKER)
def test_second(browser):
    """
    Поиск товара и добавление его в корзину через нажатие кнопки купить.
    :param browser: webdriver - объект драйвера, переданый фикстурой.
    """
    with allure.step("Открытие главной страницы интернет-магазина"):
        cart_page = CartPage(browser)
    with allure.step("Открывает страницу 'shop.mts.ru' в браузере"):
        cart_page.go()
    with allure.step("Передаем значение cookie"):
        cart_page.set_cookie_policy()
    with allure.step("Ввод названия товара  через поисковую строку 'Смартфон TECNO Camon'"):
        cart_page.add_product('Смартфон TECNO Camon')
    with allure.step("Добавление товара в корзину"):
        cart_page.cart_input()
    with allure.step("Переход в корзину"):
        cart_page.cart_count()
    with allure.step("Проверяем, что товар добавлен в корзину"):
        as_is = cart_page.get_counter()
    with allure.step("Проверка результата:Корзина не пустая"):
        assert as_is > 0, "Корзина пуста, хотя не должна быть пустой"


@allure.feature("МТС")
@allure.story("Проверка корректной работы формы 'Доставка'")
@allure.title("Проверка корректной работы формы 'Доставка' при"
              " оформлении заказа в интернет магазине МТС")
@allure.description("Тест проверяет корректную работу раздела 'Доставка',"
                    " возможность оформить доставку"
                    " заказа курьером по заданому адресу")
@allure.severity(allure.severity_level.CRITICAL)
def test_third(browser):
    """
    Поиск товара и добавление его в корзину через нажатие кнопки купить.
    Проверка возможности оформления доставки курьером по определенному адресу
    :param browser: webdriver - объект драйвера, переданый фикстурой.
    """
    with allure.step("Открытие главной страницы интернет-магазина"):
        pay_page = PayPage(browser)
    with allure.step("Открывает страницу 'shop.mts.ru' в браузере"):
        pay_page.go()
    with allure.step("Передаем значение cookie"):
        pay_page.set_cookie_policy()
    with allure.step("Ввод названия товара  через поисковую строку"):
        pay_page.add_product('Смартфон TECNO Camon')
    with allure.step("Добавление товара в корзину"):
        pay_page.cart_input()
    with allure.step("Переход в корзину"):
        pay_page.cart_count()
    with allure.step("Нажимаем кнопку 'Перейти к оформлению'"):
        pay_page.go_form_checkout()
    with allure.step("Проверяем возможность оформления доставки по адресу"):
        pay_page.get_form()
    with allure.step("Проверяем переход в раздел 'Выбор способа оплаты'"):
        pay_page.button_click()
    with allure.step("Переход осуществлен. Проверяем текст элемента с одним из способов оплаты 'Сейчас онлайн'"):
        text_element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[@class='radio-button__text']"))
        )
        expected_text = "Сейчас онлайн"
        assert expected_text in text_element.text
    # pay_page.first_name('Иван')


@allure.feature("МТС")
@allure.story("Удаление товара из корзины")
@allure.title("Удаление добавленого в корзину товара в интернет магазине МТС")
@allure.description("Тест проверяет возможность "
                    "удаления выбранного товара из корзины")
@allure.severity(allure.severity_level.BLOCKER)
def test_fourth(browser):
    """
    Удаление товара из корзины через иконку 'Мусорки'.
    :param browser: webdriver - объект драйвера, переданый фикстурой.
    """
    with allure.step("Открытие главной страницы интернет-магазина"):
        del_page = DelPage(browser)
    with allure.step("Открывает страницу 'shop.mts.ru' в браузере"):
        del_page.go()
    with allure.step("Передаем значение cookie"):
        del_page.set_cookie_policy()
    with allure.step("Ввод названия товара  через поисковую строку"):
        del_page.add_product('Смартфон TECNO Camon')
    with allure.step("Добавление товара в корзину"):
        del_page.cart_input()
    with allure.step("Переход в корзину"):
        del_page.cart_count()
    with allure.step("Удаление товара из корзины"):
        as_is = del_page.get_counter()
    with allure.step("Проверка результата:Корзина пустая"):
        assert as_is > 0, "Корзина пуста, хотя не должна быть пустой"
    with allure.step("Проверка результата:Корзина пустая"):
        del_page.del_counter()


@allure.feature("МТС")
@allure.story("Поиск товара со спецсимволами в названии")
@allure.title(
    "Поиск товара с невалидными"
    " данными в названии в интернет магазине МТС"
)
@allure.description("Тест проверяет работу строки поиска товара,"
                    " возможность найти товар с невалидным названием")
@allure.severity(allure.severity_level.CRITICAL)
def test_fifth(browser):
    """
    Поиск товара c невалидными данными в названии.
    :param browser: webdriver - объект драйвера, переданый фикстурой.
    """
    with allure.step("Открытие главной страницы интернет-магазина"):
        neg_page = NegativPage(browser)
    with allure.step("Открывает страницу 'shop.mts.ru' в браузере"):
        neg_page.go()
    with allure.step("Передаем значение cookie"):
        neg_page.set_cookie_policy()
    with allure.step("Поиск товара с невалидными данными в названии"):
        neg_page.search('$@!#^%')
    with allure.step("Проверка результата:список товаров пустой"):
        neg_page.result_search()

    # with allure.step("Проверка результата:список товаров пустой"):
    #     novalid = WebDriverWait(browser, 10).until(
    #         EC.presence_of_all_elements_located(
    #             (By.CSS_SELECTOR, ".card-name.product-card__name-link"))
    #     )
    #     novalid_text = novalid.text
    #     print(novalid_text)
        # assert len(results) > 0, "Список товаров пуст!"
        # print("Список товаров не пуст.")
