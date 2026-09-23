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
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].click();", element)

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

