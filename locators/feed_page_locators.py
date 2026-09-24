
from selenium.webdriver.common.by import By


class FeedPageLocators:
    
    ALL_TIME_COUNTER = (By.XPATH, '//div[p[contains(@class, "text_type_main-medium") and text()="Выполнено за все время:"]]/p[contains(@class, "OrderFeed_number")]')

    TODAY_COUNTER = (By.XPATH, '//div[p[contains(@class, "text_type_main-medium") and text()="Выполнено за сегодня:"]]/p[contains(@class, "OrderFeed_number")]')

    IN_PROGRESS_ORDERS = (By.XPATH, './/ul[contains(@class,"OrderFeed_orderListReady")]/li')