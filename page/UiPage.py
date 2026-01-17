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


class CartPage:

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

    
    def add_product(self, term):
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
        
        #нажимаем кнопку "Найти"
        self.__driver.find_element(
            By.XPATH, "//span[text()='Найти']").click()
        
    def cart_input(self):
        # Ждем, пока элемент станет видимым
        WebDriverWait(self.__driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, "(//div[@class='mtsds-button__text-container' and contains(text(), 'Купить')])[1]"))
        )

        # Ждем, пока элемент станет кликабельным и нажимаем кнопку "Купить"
        WebDriverWait(self.__driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='mtsds-button__text-container' and contains(text(), 'Купить')])[1]"))
        ).click()



    def cart_count(self):
        # Закрываем всплывающее окно
        element = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Закрыть']"))
        )
        self.__driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        # self.__driver.find_element(
        #    By.XPATH, "//button[@aria-label='Закрыть']").click()
        

        # Заходим в корзину   
        WebDriverWait(self.__driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-v-b4ce07b4]")))
        self.__driver.find_element(
           By.CSS_SELECTOR, "button[data-v-b4ce07b4]").click()
        
    def get_counter(self):
        #Проверяем, что счетчик не пустой
        WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='input-quantity']"))
            )
        txt = self.__driver.find_element(By.XPATH, "//input[@name='input-quantity']").get_attribute('value')
        number_str = txt.split()[0]  # Забираем только число из строки, если это необходимо
        return int(number_str)    
    