from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from element_locator_map import Locators as Ls
from generate_email_and_password import generate_random_email
from config import StoreConfig as Sc


def test_registration_error_password(driver):
    # Открытие страницы магазина
    driver.get(Sc.URL_STELLAR_BURGERS)

    #Переход в личный кабинет
    WebDriverWait(driver, Sc.TIMEOUT).until(expected_conditions.element_to_be_clickable(Ls.BUTTON_PERSONAL_ACCOUNT))
    driver.find_element(*Ls.BUTTON_PERSONAL_ACCOUNT).click()

    #Переход на страницу регистрации
    WebDriverWait(driver, Sc.TIMEOUT).until(expected_conditions.element_to_be_clickable(Ls.LINK_REG))
    driver.find_element(*Ls.LINK_REG).click()

    #Заполнение формы регистрации и нажатие кнопки "Зарегестрироваться"
    driver.find_element(*Ls.INPUT_NAME_REG).send_keys('Пользователь для авто тестов')
    random_email = generate_random_email()
    WebDriverWait(driver, Sc.TIMEOUT).until(expected_conditions.element_to_be_clickable(Ls.BUTTON_REG_REG))
    driver.find_element(*Ls.INPUT_EMAIL_REG).send_keys(random_email)
    driver.find_element(*Ls.INPUT_PASSWORD_REG).send_keys('12345')
    driver.find_element(*Ls.BUTTON_REG_REG).click()

    #Проверка успеха регистрации, редирект на форму "Авторизации"
    WebDriverWait(driver, Sc.TIMEOUT).until(expected_conditions.element_to_be_clickable(Ls.ERROR_TEXT_PASSWORD))
    assert driver.find_element(*Ls.ERROR_TEXT_PASSWORD).text == "Некорректный пароль"

