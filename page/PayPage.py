import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PayPage:

    def __init__(self, browser: WebDriver) -> None:
        self.__url = "https://shop.mts.ru/"
        self.__driver = browser

           


    def go(self):
        self.__driver.get(self.__url)

    #Передаем значение cookie
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
        WebDriverWait(self.__driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "(//div[@class='mtsds-button__text-container' and contains(text(), 'Купить')])[1]"))
        ).click()

        
    def cart_count(self):
        # Закрываем всплывающее окно
        element = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Закрыть']"))
        )
        self.__driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        
        # Заходим в корзину   
        WebDriverWait(self.__driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-v-b4ce07b4]")))
        self.__driver.find_element(
           By.CSS_SELECTOR, "button[data-v-b4ce07b4]").click()

        #Нажимаем кнопку "Перейти к оформлению"
    def  go_form_checkout(self):
        element = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "basket-promo-info__button")))
        self.__driver.execute_script("arguments[0].click();", element)

        #Нажимаем кнопку "Доставка"
    def get_form(self):
        element = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='delivery-radio-button-id'] span.radio-button__icon")))
        self.__driver.execute_script("arguments[0].click();", element)
        
        #Вводим адрес улица/дом/корпус
        address = self.__driver.find_element(By.CLASS_NAME, "address-selected__input-field")
        address.send_keys("ул, Ленина, 55")
        
        #Выбираем первый адрес из выпадающего списка
        first_item = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//button[@class='address-selected-list__button'])[1]"))
        )
        first_item = self.__driver.find_element(By.XPATH, "(//button[@class='address-selected-list__button'])[1]")
        first_item.click()

        #нажимаем кнопку "Далее"
        (WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'button--primary')]"))))
        
        self.__driver.find_element(
            By.XPATH, "//button[contains(@class, 'button--primary')]").click()
        
        #Переходим в раздел  выбора способа оплаты, по умолчанию оставляем:
        # "Сейчас онлайн Любой картой, СБП через MTS PAY". Нажимаем далее.
    def button_click(self):       
        button = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.checkout-step__button > button")))
        self.__driver.execute_script("arguments[0].click();", button)

    #     #Переходим в раздел  "Получатель". 
    #     # Заполняем данные по получателя.
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
        

               