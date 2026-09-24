from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import allure
from locators.main_page_locators import MainPageLocators

class LoginPage(BasePage):
    @allure.step('Ввести email')
    def enter_email(self, email):
        self.send_keys_to_element(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step('Ввести пароль')
    def enter_password(self, password):
        self.find_element_with_wait(LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    @allure.step('Клик на кнопку «Войти»')
    def click_login_button(self):
        self.wait_and_click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Логин в систему')
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        self.wait_for_element(MainPageLocators.CHECKOUT_BUTTON, timeout=15)
