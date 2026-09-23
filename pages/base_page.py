from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    @allure.step('Поиск элемента с ожиданием видимости')
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click_to_element(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step('Проверка наличия элемента')
    def is_element_present(self, locator):
        try:
            self.find_element_with_wait(locator)
            return True
        except:
            return False

    @allure.step('Получение текста элемента')
    def get_element_text(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Ожидание перехода на URL')
    def wait_for_url(self, expected_url):
        WebDriverWait(self.driver, self.timeout).until(EC.url_to_be(expected_url))

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Добавление текста в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)