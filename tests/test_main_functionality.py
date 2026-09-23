import allure
from pages.main_page import MainPage

from pages.login_page import LoginPage

class TestMainFunctionality:

    @allure.title('Переход по клику на «Конструктор»')
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_feed_tab()
        main_page.click_constructor_tab()
        assert main_page.is_constructor_page_opened()

    @allure.title('Переход по клику на «Лента заказов»')
    def test_navigate_to_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_feed_tab()
        assert main_page.is_feed_page_opened()

    @allure.title('Открытие всплывающего окна с деталями ингредиента')
    def test_ingredient_modal_opened(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_ingredient(0)
        assert main_page.is_ingredient_modal_opened()
        assert main_page.get_ingredient_modal_title() == "Детали ингредиента"

    @allure.title('Закрытие всплывающего окна кликом по крестику')
    def test_ingredient_modal_closed(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_ingredient(0)
        main_page.is_ingredient_modal_opened()
        main_page.close_ingredient_modal()
        assert main_page.is_ingredient_modal_closed()

    @allure.title('Увеличение счётчика ингредиента при добавлении в заказ')
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        counter_before = main_page.get_ingredient_counter(0)
        main_page.add_ingredient_to_order(0)
        counter_after = main_page.get_ingredient_counter(0)
        assert counter_after == counter_before + 2


    @allure.title('Создание заказа авторизованным пользователем')
    def test_create_order(self, driver, create_user_and_get_token):
        user = create_user_and_get_token

        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_login_account_button()

        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])

        
        main_page.add_ingredient_to_order(0)
        main_page.click_checkout_button()
        assert main_page.is_order_modal_opened()