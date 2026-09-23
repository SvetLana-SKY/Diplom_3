from selenium.webdriver.common.by import By


class MainPageLocators:
    # Вкладки навигации
    CONSTRUCTOR_TAB = (By.XPATH, '//a[@href="/" and .//p[text()="Конструктор"]]')
    FEED_TAB = (By.XPATH, '//a[@href="/feed" and .//p[text()="Лента Заказов"]]')
    CONSTRUCTOR_TITLE = (By.XPATH, '//h1[text()="Соберите бургер"]')
    FEED_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, '//p[contains(text(), "Личный Кабинет")]')

    # Карточки ингредиентов
    INGREDIENT_CARDS = (By.XPATH, '//a[contains(@class, "BurgerIngredient_ingredient__")]')

    # Модальное окно ингредиента
    INGREDIENT_MODAL = (By.XPATH, '//div[contains(@class, "Modal_modal__contentBox__")]')
    INGREDIENT_MODAL_TITLE = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    INGREDIENT_MODAL_CLOSE = (By.CSS_SELECTOR, '[class*="Modal_modal__close"]')

    # Корзина заказа
    ORDER_BASKET = (By.CSS_SELECTOR, 'ul[class*="BurgerConstructor_basket__list"]')

    # Счётчик ингредиента (относительный — ищется внутри карточки)
    INGREDIENT_COUNTER = (By.XPATH, './/div[contains(@class, "counter_counter__")]')

    # Кнопка оформления заказа
    CHECKOUT_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

    # Модальное окно с номером заказа
    ORDER_MODAL = (By.XPATH, '//h2[contains(@class, "Modal_modal__title__") and contains(@class, "text_type_digits-large")]')
    ORDER_MODAL_CLOSE = (By.CSS_SELECTOR, '[class*="Modal_modal__close"]')