import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.feed_page import OrderFeedPage


class TestFeed:

    @allure.title('Счётчик «Выполнено за всё время» увеличивается при создании заказа')
    def test_all_time_counter_increases(self, driver, create_user_and_get_token):
        user = create_user_and_get_token

        # Запоминаем счётчик до создания заказа
        feed_page = OrderFeedPage(driver)
        feed_page.open_feed_page()
        counter_before = feed_page.get_all_time_counter()

        # Логинимся
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_login_account_button()

        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])

        # Возвращаемся в конструктор и оформляем заказ
        main_page.click_constructor_tab()
        main_page.add_ingredient_to_order(0)
        main_page.click_checkout_button()
        main_page.wait_for_order_number()
        

        # Возвращаемся в ленту и проверяем счётчик
        feed_page.open_feed_page()
        counter_after = feed_page.get_all_time_counter()

        assert int(counter_before) < int(counter_after)


    @allure.title('Счётчик «Выполнено за сегодня» увеличивается при создании заказа')
    def test_today_counter_increases(self, driver, create_user_and_get_token):
        user = create_user_and_get_token

        # Запоминаем счётчик до создания заказа
        feed_page = OrderFeedPage(driver)
        feed_page.open_feed_page()
        counter_before = feed_page.get_today_counter()

        # Логинимся
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_login_account_button()

        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])

        # Возвращаемся в конструктор и оформляем заказ
        main_page.click_constructor_tab()
        main_page.add_ingredient_to_order(0)
        main_page.click_checkout_button()
        main_page.wait_for_order_number()

        # Возвращаемся в ленту и проверяем счётчик
        feed_page.open_feed_page()
        counter_after = feed_page.get_today_counter()

        assert int(counter_before) < int(counter_after)


    @allure.title('Номер нового заказа появляется в разделе «В работе»')
    def test_order_appears_in_progress(self, driver, create_user_and_get_token):
        user = create_user_and_get_token
        feed_page = OrderFeedPage(driver)
        
        # Логинимся
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_login_account_button()

        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])

        # Оформляем заказ и запоминаем номер
        main_page.click_constructor_tab()
        main_page.add_ingredient_to_order(0)
        main_page.click_checkout_button()
        order_id = main_page.wait_for_order_number()

        # Идём в ленту заказов
        
        
        feed_page.open_feed_page()
        feed_page.wait_for_order_id_in_progress()
        # Проверяем, что номер заказа есть в разделе «В работе»
        in_progress_text = feed_page.get_orders_in_progress()

        assert order_id in in_progress_text