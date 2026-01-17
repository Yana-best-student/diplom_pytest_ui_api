import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class UiPage:

    def __init__(self, browser: WebDriver) -> None:
        self.__url = "https://shop.mts.ru/"
        self.__driver = browser

    def go(self):
        self.__driver.get(self.__url)

    def set_cookie_policy(self):
        cookie = {
            "name": "COOKIES_MASSAGE_APPLY",
            "value": "true"
        }
        self.__driver.add_cookie(cookie)


    def search(self, term):
        #Ожидаем появления поля поиска
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='q']"))))

        self.__driver.find_element(
            By.CSS_SELECTOR, "input[name='q']").click()

        #Вводим в строку поиска название товара
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.XPATH, "//input[@id='search-popup-field']"))))
        self.__driver.find_element(
            By.XPATH, "//input[@id='search-popup-field']").send_keys(term)

        self.__driver.find_element(
            By.XPATH, "//span[text()='Найти']").click()
    
    