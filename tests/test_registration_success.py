from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from element_locator_map import Locators as Ls
from generate_email_and_password import generate_random_email, generate_random_password


driver = webdriver.Chrome()
#Открытие страницы магазина
driver.get("https://stellarburgers.nomoreparties.site/")

#Переход в личный кабинет
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Ls.BUTTON_PERSONAL_ACCOUNT))
driver.find_element(*Ls.BUTTON_PERSONAL_ACCOUNT).click()

#Переход на страницу регистрации
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Ls.LINK_REG))
driver.find_element(*Ls.LINK_REG).click()

#Заполнение формы регистрации и нажатие кнопки "Зарегестрироваться"
driver.find_element(*Ls.INPUT_NAME_REG).send_keys('Пользователь для авто тестов')
random_email = generate_random_email()
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Ls.BUTTON_REG_REG))
driver.find_element(*Ls.INPUT_EMAIL_REG).send_keys(random_email)
random_password = generate_random_password()
driver.find_element(*Ls.INPUT_PASSWORD_REG).send_keys(random_password)
driver.find_element(*Ls.BUTTON_REG_REG).click()

#Проверка успеха регистрации, редирект на форму "Авторизации"
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Ls.BUTTON_AUTH_SIGN_IN))
assert driver.find_element(*Ls.BUTTON_AUTH_SIGN_IN).text == "Войти"

driver.quit()
