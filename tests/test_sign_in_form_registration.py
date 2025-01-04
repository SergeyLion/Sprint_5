from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from element_locator_map import Locators as Ls


driver = webdriver.Chrome()
#Открытие страницы магазина
driver.get("https://stellarburgers.nomoreparties.site/")

#Переход в личный кабинет
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Ls.BUTTON_PERSONAL_ACCOUNT))
driver.find_element(*Ls.BUTTON_PERSONAL_ACCOUNT).click()

#Переход на страницу регистрации
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Ls.LINK_REG))
driver.find_element(*Ls.LINK_REG).click()

#Переход на форму "Вход"
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Ls.LINK_AUTH))
driver.find_element(*Ls.LINK_AUTH).click()

#Заполнение формы "Вход" и нажатие кнопки "Войти"
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Ls.BUTTON_AUTH_SIGN_IN))
driver.find_element(*Ls.INPUT_EMAIL_AUTH).send_keys("sergeylvov17777@yandex.ru")
driver.find_element(*Ls.INPUT_PASSWORD_AUTH).send_keys("123654789")
driver.find_element(*Ls.BUTTON_AUTH_SIGN_IN).click()

#Проверка наличия кнопки "Оформить заказ" на главной странице
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Ls.BUTTON_ORDER_MAIN_PAGE))
assert driver.find_element(*Ls.BUTTON_ORDER_MAIN_PAGE).text == "Оформить заказ"

driver.quit()
