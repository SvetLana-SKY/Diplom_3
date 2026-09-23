from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import allure


class MainPage(BasePage):

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.driver.get(Urls.MAIN_PAGE_URL)

    @allure.step('Клик на вкладку «Конструктор»')
    def click_constructor_tab(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_TAB)

    @allure.step('Клик на вкладку «Лента заказов»')
    def click_feed_tab(self):
        self.click_to_element(MainPageLocators.FEED_TAB)

    @allure.step('Клик по ингредиенту')
    def click_ingredient(self, index=0):
        ingredients = self.driver.find_elements(*MainPageLocators.INGREDIENT_CARDS)
        ingredients[index].click()

    @allure.step('Проверка, что модальное окно ингредиента открыто')
    def is_ingredient_modal_opened(self):
        return self.is_element_present(MainPageLocators.INGREDIENT_MODAL)

    @allure.step('Получить заголовок модального окна ингредиента')
    def get_ingredient_modal_title(self):
        return self.get_element_text(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step('Закрыть модальное окно ингредиента')
    def close_ingredient_modal(self):
        self.click_to_element(MainPageLocators.INGREDIENT_MODAL_CLOSE)

    @allure.step('Проверка, что модальное окно ингредиента закрыто')
    def is_ingredient_modal_closed(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_MODAL)
        )

    @allure.step('Получить значение счётчика ингредиента')
    def get_ingredient_counter(self, index=0):
        ingredients = self.driver.find_elements(*MainPageLocators.INGREDIENT_CARDS)
        counters = ingredients[index].find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        if counters:
            return int(counters[0].text)
        return 0

    @allure.step('Добавить ингредиент в заказ (drag-and-drop)')
    def add_ingredient_to_order(self, index=0):
        self.find_element_with_wait(MainPageLocators.INGREDIENT_CARDS)
        ingredients = self.driver.find_elements(*MainPageLocators.INGREDIENT_CARDS)
        basket = self.find_element_with_wait(MainPageLocators.ORDER_BASKET)

        script = """
        function simulateDragDrop(source, target) {
            var dt = new DataTransfer();
            source.dispatchEvent(new DragEvent('dragstart', {bubbles: true, dataTransfer: dt}));
            target.dispatchEvent(new DragEvent('dragenter', {bubbles: true, dataTransfer: dt}));
            target.dispatchEvent(new DragEvent('dragover', {bubbles: true, dataTransfer: dt}));
            target.dispatchEvent(new DragEvent('drop', {bubbles: true, dataTransfer: dt}));
            source.dispatchEvent(new DragEvent('dragend', {bubbles: true, dataTransfer: dt}));
        }
        simulateDragDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(script, ingredients[index], basket)

    @allure.step('Клик на кнопку «Оформить заказ»')
    def click_checkout_button(self):
        self.click_to_element(MainPageLocators.CHECKOUT_BUTTON)

    @allure.step('Проверка, что модальное окно заказа открыто')
    def is_order_modal_opened(self):
        return self.is_element_present(MainPageLocators.ORDER_MODAL)


    @allure.step('Проверка, что tесть заголовок конструктора')
    def is_constructor_page_opened(self):
        return self.is_element_present(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Проверка, что есть заголовок лента заказов')
    def is_feed_page_opened(self):
        return self.is_element_present(MainPageLocators.FEED_TITLE)

    @allure.step('Клик на кнопку «Личный Кабинет»')
    def click_login_account_button(self):
        self.click_to_element(MainPageLocators.LOGIN_ACCOUNT_BUTTON)