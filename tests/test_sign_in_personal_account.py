from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from element_locator_map import Locators as Ls
from config import StoreConfig as Sc


driver = webdriver.Chrome()
#Открытие страницы магазина
driver.get(Sc.URL_STELLAR_BURGERS)

#Переход в личный кабинет
WebDriverWait(driver, Sc.TIMEOUT).until(expected_conditions.element_to_be_clickable(Ls.BUTTON_PERSONAL_ACCOUNT))
driver.find_element(*Ls.BUTTON_PERSONAL_ACCOUNT).click()

#Заполнение формы "Вход" и нажатие кнопки "Войти"
WebDriverWait(driver, Sc.TIMEOUT).until(expected_conditions.element_to_be_clickable(Ls.BUTTON_AUTH_SIGN_IN))
driver.find_element(*Ls.INPUT_EMAIL_AUTH).send_keys(Sc.AUTH_USERNAME)
driver.find_element(*Ls.INPUT_PASSWORD_AUTH).send_keys(Sc.AUTH_PASSWORD)
driver.find_element(*Ls.BUTTON_AUTH_SIGN_IN).click()

#Проверка наличия кнопки "Оформить заказ" на главной странице
WebDriverWait(driver, Sc.TIMEOUT).until(expected_conditions.element_to_be_clickable(Ls.BUTTON_ORDER_MAIN_PAGE))
assert driver.find_element(*Ls.BUTTON_ORDER_MAIN_PAGE).text == "Оформить заказ"

driver.quit()
