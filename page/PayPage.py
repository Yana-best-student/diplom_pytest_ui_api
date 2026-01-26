import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PayPage:

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
    def add_product(self, term):
        """
        Ожидаем появления поля поиска, кликаем на него.
        """
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located(
             (By.CSS_SELECTOR, "input[name='q']"))))

        self.__driver.find_element(
            By.CSS_SELECTOR, "input[name='q']").click()
        """
        Вводим в строку поиска название товара 'Смартфон TECNO Camon 40'.
        """
        (WebDriverWait(self.__driver, 10).until
         (EC.visibility_of_element_located(
             (By.XPATH, "//input[@id='search-popup-field']"))))
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
        WebDriverWait(self.__driver, 30).until(
            EC.visibility_of_element_located
            ((By.XPATH, "(//div[@class='mtsds-button__text-container' and contains(text(), 'Купить')])[1]"))
            ).click()

    @allure.step("Переход в корзину")
    def cart_count(self):
        """
        Закрываем окно с предложением 'Собрать выгодный
        комплект', нажатием на иконку
        крестика в правом верхнем углу.
        """
        element = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@aria-label='Закрыть']"))
        )
        self.__driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        WebDriverWait(self.__driver, 30).until
        (EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "button[data-v-b4ce07b4]")))
        """
        Нажимаем на иконку корзины, ожидая пока она станет видимой
        """
        self.__driver.find_element(
            By.CSS_SELECTOR, "button[data-v-b4ce07b4]").click()

    @allure.step("Переход к оформлению покупки")
    def go_form_checkout(self):
        """
        Нажимаем кнопку 'Перейти к оформлению'
        """
        element = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "basket-promo-info__button")))
        self.__driver.execute_script("arguments[0].click();", element)

    @allure.step("Оформляем покупку с доставкой по адресу")
    def get_form(self):
        """
        Нажимаем  поле'Доставка', ожидая пока оно станет кликабельным
        """
        element = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "label[for='delivery-radio-button-id'] span.radio-button__icon")))
        self.__driver.execute_script("arguments[0].click();", element)

        """
        Заполняем  строку улица/дом/корпус.
        Вводим валидные значения 'Ленина 55'
        """
        address = self.__driver.find_element(
            By.CLASS_NAME, "address-selected__input-field")
        address.send_keys("ул, Ленина, 55")

        """
        Открывается выпадающий список с доступными адресами доставки.
        Кликаем на первый адрес из выпадающего списка.
        """
        first_item = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "(//button[@class='address-selected-list__button'])[1]"))
        )
        first_item = self.__driver.find_element(
            By.XPATH, "(//button[@class='address-selected-list__button'])[1]")
        first_item.click()

        """
        Нажимаем кнопку 'Далее' для перехода в форму выбора способа оплаты.
        """
        (WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[contains(@class, 'button--primary')]"))))

        self.__driver.find_element(
            By.XPATH, "//button[contains(@class, 'button--primary')]").click()

    @allure.step("Выбор способа оплаты 'Сейчас онлайн Любой картой, СБП через MTS PAY'")
    def button_click(self):
        """
        Переходим в раздел  выбора способа оплаты:
        'Сейчас онлайн Любой картой, СБП через MTS PAY'.
        """
        
        WebDriverWait(self.__driver, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[@class='radio-button__text']"))).click()
        
        

        # button = WebDriverWait(self.__driver, 30).until(
        #     EC.element_to_be_clickable(
        # (By.XPATH, "//button[contains(@class, 'button--primary') and text()='Далее']")))
        # self.__driver.execute_script("arguments[0].click();", button)
        # button.click()

    #     #Переходим в раздел  "Получатель".
    #     # Заполняем данные  получателя.
    # def first_name(self, name):
    #     WebDriverWait(self.__driver, 10).until(
    #         EC.visibility_of_element_located((By.ID, "user-firstname"))
    #         )
    #     first = self.__driver.find_element(By.ID, "user-firstname")
    #     self.__driver.execute_script("arguments[0].scrollIntoView();", first)
    #     first.clear()
    #     first.send_keys(name)

# # Заполняем фамилию
#     def last_name(self, surname):
#         WebDriverWait(self.__driver, 10).until(
#             EC.visibility_of_element_located((By.ID, "user-lastname"))
#             )
#         self.__driver.find_element(By.ID, "user-lastname").send_keys(surname)
