from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from element_locator_map import Locators as Ls
from config import StoreConfig as Sc


def test_tab_bun_scroll_to_bun(driver):
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

    #Нажатие на таб "Начинка"
    WebDriverWait(driver, Sc.TIMEOUT).until(expected_conditions.element_to_be_clickable(Ls.TAB_TOPPING))
    driver.find_element(*Ls.TAB_TOPPING).click()

    #Нажатие на таб "Булки"
    WebDriverWait(driver, Sc.TIMEOUT).until(expected_conditions.element_to_be_clickable(Ls.TAB_BUN))
    driver.find_element(*Ls.TAB_BUN).click()

    #Проверка активности таба "Булки"
    assert "tab_tab_type_current" in driver.find_element(*Ls.TAB_BUN).get_attribute('class')

