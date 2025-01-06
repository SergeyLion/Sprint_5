from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from element_locator_map import Locators as Ls
from config import StoreConfig as Sc


driver = webdriver.Chrome()
def test_sign_out():
    #Открытие страницы магазина
    driver.get(Sc.URL_STELLAR_BURGERS)

    #Переход на форму "Вход" с главной странице
    WebDriverWait(driver, Sc.TIMEOUT).until(expected_conditions.element_to_be_clickable(Ls.BUTTON_SIGN_IN_MAIN_PAGE))
    driver.find_element(*Ls.BUTTON_SIGN_IN_MAIN_PAGE).click()

    #Заполнение формы "Вход" и нажатие кнопки "Войти"
    WebDriverWait(driver, Sc.TIMEOUT).until(expected_conditions.element_to_be_clickable(Ls.BUTTON_AUTH_SIGN_IN))
    driver.find_element(*Ls.INPUT_EMAIL_AUTH).send_keys(Sc.AUTH_USERNAME)
    driver.find_element(*Ls.INPUT_PASSWORD_AUTH).send_keys(Sc.AUTH_PASSWORD)
    driver.find_element(*Ls.BUTTON_AUTH_SIGN_IN).click()

    #Переход в личный кабинет
    WebDriverWait(driver, Sc.TIMEOUT).until(expected_conditions.element_to_be_clickable(Ls.BUTTON_PERSONAL_ACCOUNT))
    driver.find_element(*Ls.BUTTON_PERSONAL_ACCOUNT).click()

    #Нажатие на кнопку "Выход" в личном кабинете
    WebDriverWait(driver, Sc.TIMEOUT).until(expected_conditions.element_to_be_clickable(Ls.BUTTON_SIGN_OUT))
    driver.find_element(*Ls.BUTTON_SIGN_OUT).click()

    #Проверка наличия кнопки "Войти" в форме "Вход"
    WebDriverWait(driver, Sc.TIMEOUT).until(expected_conditions.visibility_of_element_located(Ls.BUTTON_AUTH_SIGN_IN))
    assert driver.find_element(*Ls.BUTTON_AUTH_SIGN_IN).text == "Войти"


    driver.quit()
