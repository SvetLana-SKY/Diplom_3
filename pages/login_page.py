from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators

class LoginPage(BasePage):

    @allure.step('Ввести email')
    def enter_email(self, email):
        self.find_element_with_wait(LoginPageLocators.EMAIL_INPUT).send_keys(email)

    @allure.step('Ввести пароль')
    def enter_password(self, password):
        self.find_element_with_wait(LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    @allure.step('Клик на кнопку «Войти»')
    def click_login_button(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        self.click_to_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Логин в систему')
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
    
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(MainPageLocators.CHECKOUT_BUTTON
            )
        )
