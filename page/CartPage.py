import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

load_dotenv()

class CartPage:

    def __init__(self, browser: WebDriver) -> None:
        """
        Конструктор класса PageObject.
        :param driver: Webdriver — объект драйвера Selenium.
        """
        self.__url = os.getenv("UI_URL")
        self.__driver = browser

    @allure.step("Открытие главной страницы интернет-магазина")
    def go(self):
        """
        Открывает страницу "shop.mts.ru" в браузере,
        использует driver.get для открытия страницы
        """
        self.__driver.get(self.__url)

    @allure.step("Передаем значение cookie")
    def set_cookie_policy(self):
        cookie = {
            "name": "COOKIES_MASSAGE_APPLY",
            "value": "true"
        }
        self.__driver.add_cookie(cookie)

    @allure.step("Поиск товара через поисковую строку")
    def add_product(self, term):
        """
        Ожидаем появления поля поиска, кликаем на него.
        """
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located
               ((By.CSS_SELECTOR, "input[name='q']"))))

        self.__driver.find_element(
            By.CSS_SELECTOR, "input[name='q']").click()

        """
        Вводим в строку поиска название товара 'Смартфон TECNO Camon 40'.
        """
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located
               ((By.XPATH, "//input[@id='search-popup-field']"))))
        self.__driver.find_element(
            By.XPATH, "//input[@id='search-popup-field']").send_keys(term)

        """
        нажимаем кнопку "Найти".
        """
        self.__driver.find_element(
            By.XPATH, "//span[text()='Найти']").click()

    @allure.step("Добавление товара в корзину")
    def cart_input(self):
        """
        Ждем, пока кнопка 'Купить' станет видимой, нажимаем на кнопку.
        """
        WebDriverWait(self.__driver, 30).until(EC.visibility_of_element_located(
            (By.XPATH, "(//div[@class='mtsds-button__text-container' and contains(text(), 'Купить')])[1]"))).click()

    @allure.step("Переход в корзину")
    def cart_count(self):
        """
        Закрываем окно с предложением 'Собрать выгодный комплект'
        нажатием на иконку крестика в правом верхнем углу.
        """
        element = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@aria-label='Закрыть']"))
        )
        self.__driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        """
        Нажимаем на иконку корзины, ожидая пока она станет видимой
        """
        WebDriverWait(self.__driver, 30).until(
            EC.visibility_of_element_located
            ((By.CSS_SELECTOR, "button[data-v-b4ce07b4]")))
        self.__driver.find_element(
            By.CSS_SELECTOR, "button[data-v-b4ce07b4]").click()

    @allure.step("Проверяем, что товар добавлен в корзину")
    def get_counter(self):
        """
        Проверяем, что счетчик корзины не пустой
        """
        WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@name='input-quantity']"))
        )
        txt = self.__driver.find_element(
            By.XPATH, "//input[@name='input-quantity']").get_attribute('value')
        number_str = txt.split()[0]
        return int(number_str)
