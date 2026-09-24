
import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators

from urls import Urls


class OrderFeedPage(BasePage):

    @allure.step('Открыть ленту заказов')
    def open_feed_page(self):
        self.open(Urls.FEED_PAGE_URL)

    @allure.step('Получить значение счётчика «Выполнено за всё время»')
    def get_all_time_counter(self):
        return int(self.find_element_with_wait(FeedPageLocators.ALL_TIME_COUNTER).text)


    @allure.step('Получить значение счётчика «Выполнено за сегодня»')
    def get_today_counter(self):
        return int(self.find_element_with_wait(FeedPageLocators.TODAY_COUNTER).text)


    @allure.step('Получить данные о заказах в работе')
    def get_orders_in_progress(self):
        self.find_element_with_wait(FeedPageLocators.IN_PROGRESS_ORDERS)
        element_text = self.get_element_text(FeedPageLocators.IN_PROGRESS_ORDERS)
        return element_text

    @allure.step('Подождать, когда появится номер заказа в работе')
    def wait_for_order_id_in_progress(self):
        order_id = 'Все текущие заказы готовы!'
        while order_id == 'Все текущие заказы готовы!':
            order_id = self.get_element_text(FeedPageLocators.IN_PROGRESS_ORDERS)
        return order_id

