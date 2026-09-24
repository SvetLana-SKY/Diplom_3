from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10


    @allure.step('Открыть страницу по URL')
    def open(self, url):
        self.driver.get(url)


    @allure.step('Поиск элемента с ожиданием видимости')
    def find_element_with_wait(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Поиск всех элементов')
    def find_elements_with_wait(self, locator):
        return self.driver.find_elements(*locator)

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


    @allure.step('Ожидание кликабельности элемента')
    def wait_and_click(self, locator, timeout=None):
        element = WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ввод текста в поле')
    def send_keys_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Ожидание видимости элемента')
    def wait_for_element(self, locator, timeout=None):
        self.find_element_with_wait(locator, timeout)


    @allure.step('Ожидание невидимости элемента')
    def wait_for_invisibility(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step('Выполнение JavaScript')
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

