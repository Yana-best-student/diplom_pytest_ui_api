# diplom_pytest_ui_api

## Шаблон для автоматизации тестирования на python

### Шаги

1. Склонировать проект `git clone [репозиторий](https://github.com/Yana-best-student/diplom_pytest_ui_api.git)`
2. Установить все зависимости pip3 install > -r requirements.txt
3. Запустить тесты 'pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'
6. Выполнить команду pip install -r requirements.txt в терминале.
7. Создать файл .env в корне проекта и добавить в него переменные:

- [API_URL](https://shop.mts.ru/apigw/api/v1/search/hits)
- [UI_URL](https://shop.mts.ru/)
- API_TOKEN=Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJ3ZWIiLCJqdGkiOiI2MWNmNjJjNTExMDc5NzE2NWY0MmQ4ZWRjMDZlYzc0NDM5MWFlZmZiMDM1MjFiNmI3N2Y5ODNjMTVkZGM4ZDNkNmVkNGUwZWVjYzRiMGUxZiIsImlhdCI6MTc1Njk5ODk0MS43NTc3NDYsIm5iZiI6MTc1Njk5ODk0MS43NTc3NDgsImV4cCI6MTc1NzAzNDk0MS42MzEwNzgsInN1YiI6Ijg1MzM4ZTkyLWQ2NDYtNGM0My1iY2Q4LWI5MDhiZjM1NGMyNiIsInNjb3BlcyI6W10sImV4dGVybmFsSWQiOiJlM2EzNTI2MC0xNTVmLTExZWItODllZi03YjhkMjVhYTQxNGIiLCJzb3VyY2UiOiJ3ZWJzc28iLCJwaG9uZSI6Ijc5OTIyMjcwMjUwIiwicm9sZXMiOlsiUk9MRV9VU0VSIl0sImNhc2hiYWNrU3RhdHVzIjp7InByZW1pdW1TdGF0dXMiOiJOT19QUkVNSVVNIiwicmVnaXN0ZXJlZCI6dHJ1ZSwiY3JlYXRlZEF0IjoiMjAyNS0wOC0yOFQxNDozODoxMSswMzowMCIsInVwZGF0ZWRBdCI6IjIwMjUtMDktMDRUMTg6MTU6NDErMDM6MDAifX0.HfDcWk_N438uZ_wajJkSoRFAufp4k020Uagad54MCGp1-3FTgbfrQSzMfPxv8UWsk0_hhCYw8y3bmez-6hd6iAVHWUOW6qtc3QaEKRU4yj6zUK0-LzffNUV34iu00O0p1AwyIpYtPdzRVzQocudzMZ17vkrqJKKiz6JUStcQ6IGQxEzdJTBkNSDGNhgmfasf3aXZeSZFlNBaagD_Acf4FoLn3yFDw5rx56JZ738zdirpY-qwfkmRPW6RFZJLSr47HKPPdStXzsui5MHRsHwbcuF4iQ9aA3HS-VC3t-zKDDF2_ADzz2uPljp3ns8cva4WvWZ3gK3KNVGz_X5chjIVkA

### Стек

- pytest
- selenium
- webdriver manager
- requests
- _sqlalchemy_
- allure
- configparser
- json

### Струткура

- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД
- ./configuration - провайдер настроек
- test_config.ini - настройки для тестов
- ./testdata - провайдер тестовых данных
- test_data.json

### Полезные ссылки

- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)
- [Про pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)
