from selenium.webdriver.common.by import By


class Locators:
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(),'Кабинет')]") #Кнопка "Личный кабенет"
    LINK_REG = (By.XPATH, "//a[contains(@class,'Auth_link') and contains(text(),'Зарегистрироваться')]") #Ссылка "Зарегистрироваться" в форме "Вход"
    INPUT_NAME_REG = (By.XPATH, "//fieldset[1]/div/div/input") #Поле ввода "Имя" формы "Регистрация"
    INPUT_EMAIL_REG = (By.XPATH, "//fieldset[2]/div/div/input") #Поле ввода "Email" формы "Регистрация"
    INPUT_PASSWORD_REG = (By.NAME, "Пароль") #Поле ввода "Пароль" формы "Регистрация"
    BUTTON_REG_REG = (By.XPATH, "//button[text()='Зарегистрироваться']") #Кнопка "Зарегистрироваться" формы "Регистрация"
    BUTTON_AUTH_SIGN_IN = (By.XPATH, "//button[text()='Войти']") #Кнопка "Войти" формы "Вход"
    ERROR_TEXT_PASSWORD = (By.XPATH, "//p[text() = 'Некорректный пароль']") #Текст ошибки "Некорректный пароль" для поля ввода "Пароль"
    BUTTON_SIGN_IN_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']") #Кнопка "Войти в аккаунт" на главной странице
    INPUT_EMAIL_AUTH = (By.XPATH, "//fieldset[1]/div/div/input") #Поле ввода "Email" формы "Вход"
    INPUT_PASSWORD_AUTH = (By.NAME, "Пароль") #Поле ввода "Пароль" формы "Вход"
    BUTTON_ORDER_MAIN_PAGE = (By.XPATH, "//button[text()='Оформить заказ']") #Кнопка "Оформить заказ" на главной странице
    LINK_AUTH = (By.XPATH, "//a[contains(@class,'Auth_link') and contains(text(),'Войти')]") #Ссылка "Войти" в форме "Регистрация"
    LINK_RESET_PASSWORD = (By.XPATH, "//a[contains(@class,'Auth_link') and contains(text(),'Восстановить пароль')]")  # Ссылка "Восстановить пароль" в форме "Регистрация"
    INPUT_LOGIN_PROFILE = (By.XPATH, "//li[2]/div/div/input")  # Поле ввода "Логин" формы "Профиль"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор в хедере программы
    LINK_LOGO = (By.XPATH, "//div[contains(@class,'header__logo')]/a")  # Ссылка на домашнюю страницу в логотипе "Stellar Burgers"
    BUTTON_SIGN_OUT = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход" в личном кабинете
    TAB_BUN = (By.XPATH, "//div[@style='display: flex;']/div[1]")  # Таб "Булки" в конструкторе
    TAB_SAUCE = (By.XPATH, "//div[@style='display: flex;']/div[2]")  # Таб "Соусы" в конструкторе
    TAB_TOPPING = (By.XPATH, "//div[@style='display: flex;']/div[3]")  # Таб "Начинки" в конструкторе

