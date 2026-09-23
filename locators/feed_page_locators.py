
from selenium.webdriver.common.by import By


class FeedPageLocators:
    # Счётчик «Выполнено за все время»
    ALL_TIME_COUNTER = (By.XPATH, '//div[p[contains(@class, "text_type_main-medium") and text()="Выполнено за все время:"]]/p[contains(@class, "OrderFeed_number")]')

    # Счётчик «Выполнено за сегодня»
    TODAY_COUNTER = (By.XPATH, '//div[p[contains(@class, "text_type_main-medium") and text()="Выполнено за сегодня:"]]/p[contains(@class, "OrderFeed_number")]')
    # Заказы в разделе «В работе»
    IN_PROGRESS_ORDERS = (By.XPATH, './/ul[contains(@class,"OrderFeed_orderListReady")]/li')