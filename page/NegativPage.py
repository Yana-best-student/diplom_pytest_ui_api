import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class NegativPage:

    def __init__(self, browser: WebDriver) -> None:
        """
        Конструктор класса PageObject.
        :param driver: Webdriver — объект драйвера Selenium.
        """
        self.__url = "https://shop.mts.ru/"
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
    def search(self, term):
        """
        Ожидаем появления поля поиска, кликаем на него.
        """
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='q']"))))

        self.__driver.find_element(
            By.CSS_SELECTOR, "input[name='q']").click()

        """
        Вводим в строку поиска невалидное название товара '$@!#^%'.
        """
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.XPATH, "//input[@id='search-popup-field']"))))
        self.__driver.find_element(
            By.XPATH, "//input[@id='search-popup-field']").send_keys(term)

        """
        нажимаем кнопку "Найти".
        """
        self.__driver.find_element(
            By.XPATH, "//span[text()='Найти']").click()

        novalid = WebDriverWait(self.__driver, 30).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".search-no-results-block__content .search-no-results-block__title"))
        )
        novalid_text = novalid.text
        print(novalid_text)

        """
        Появляется текст 'Ничего не нашлось'
        """
        if "Ничего не нашлось" in novalid_text:
            print("уточните запрос.")
