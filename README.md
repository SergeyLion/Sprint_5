# Sprint_5
## Набор тестов для магазина "Stellar Burgers" 

Были созданы вспомогательные файлы: 
* config.py - Описаны константы для тестов
* element_locator_map.py - описаны локаторы для тестов
* generate_email_and_password.py - две функции для генерации Логотипа и Пароля
* requirements.txt - файлс с внешними зависимостями

Реализованы следующие тесты: 
* test_tab_topping_scroll_to_topping.py - Проверяет выбор таба "Начинка" и скролл к разделу "Начинки"
* test_tab_sauce_scroll_to_sauce.py - Проверяет выбор таба "Соусы" и скролл к разделу "Соусы"
* test_tab_bun_scroll_to_bun.py - Проверяет выбор таба "Булки" и скролл к разделу "Булки"
* test_sign_out.py - Проверяет выход из аккаунта 
* test_sign_in_personal_account.py - Проверяет вход через личный кабинет
* test_sign_in_homepage_button.py - Проверяет вход через кнопку "Вход" на главной странице
* test_sign_in_form_reset_password.py - Проверяет вход через форму "Восстановления пароля"
* test_sign_in_form_registration.py - Проверяет вход через кнопку в форме регистрации
* test_registration_error_password.py - Проверяет ошибку для некоректного пароля в форме регистрации
* test_registration_success.py - Проверяет успешность регистрации 
* test_navigation_to_personal_account.py - Проверяет переход по клику на кнопку "Личный кабинет"
* test_navigation_to_homepage.py - Проверяет переход на домашнию страницу по клику на логотип
* test_navigation_to_constructor.py - Проверяет переход на страницу конструктора по клику на кнопку "Конструктор" 