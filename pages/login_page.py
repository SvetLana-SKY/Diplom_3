from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

import allure


class LoginPage(BasePage):

    @allure.step('Ввести email')
    def enter_email(self, email):
        self.find_element_with_wait(LoginPageLocators.EMAIL_INPUT).send_keys(email)
  

    @allure.step('Ввести пароль')
    def enter_password(self, password):
        self.find_element_with_wait(LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    @allure.step('Клик на кнопку «Войти»')
    def click_login_button(self):
        button = self.find_element_with_wait(LoginPageLocators.LOGIN_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)
   

    @allure.step('Логин в систему')
    def login(self, email, password):
        
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
