from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Поле email — ищем по type="text" и name="name"
    EMAIL_INPUT = (By.XPATH, '//input[@type="text" and @name="name"]')

    # Поле пароля — ищем по type="password"
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]')

    # Кнопка «Войти»
    LOGIN_BUTTON = (By.XPATH, '//form[contains(@class, "Auth_form")]//button[text()="Войти"]')