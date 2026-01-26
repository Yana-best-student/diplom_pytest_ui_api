import allure
import pytest
from selenium import webdriver
from configuration.ConfigProvider import ConfigProvider


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        timeout = ConfigProvider().getint("ui", "timeout")
        browser = webdriver.Chrome()
        browser.implicitly_wait(timeout)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()
