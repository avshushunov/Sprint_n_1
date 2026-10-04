from selenium.webdriver.common.by import By

class RouteBlockLocators:
    TYPE_PICKER = (By.CSS_SELECTOR, ".type-picker.shown")
    TAB_OPTIMAL = (By.XPATH, "//div[contains(@class, 'mode') and text()='Оптимальный']")
    TAB_FAST = (By.XPATH, "//div[contains(@class, 'mode') and text()='Быстрый']")
    TAB_CUSTOM = (By.XPATH, "//div[contains(@class, 'mode') and text()='Свой']")

    TYPES_CONTAINER = (By.CSS_SELECTOR, ".types-container")
    TRANSPORT_CAR = (By.XPATH, "//img[contains(@class, 'type-icon') and contains(@src, 'car')]/parent::div")
    TRANSPORT_WALK = (By.XPATH, "//img[contains(@class, 'type-icon') and contains(@src, 'walk')]/parent::div")
    TRANSPORT_TAXI = (By.XPATH, "//img[contains(@class, 'type-icon') and contains(@src, 'taxi')]/parent::div")
    TRANSPORT_BIKE = (By.XPATH, "//img[contains(@class, 'type-icon') and contains(@src, 'bike')]/parent::div")
    TRANSPORT_SCOOTER = (By.XPATH, "//img[contains(@class, 'type-icon') and contains(@src, 'scooter')]/parent::div")
    TRANSPORT_DRIVE = (By.XPATH, "//img[contains(@class, 'type-icon') and contains(@src, 'drive')]/parent::div")

    ROUTE_COST = (By.CSS_SELECTOR, ".results-text .text")
    ROUTE_DURATION = (By.CSS_SELECTOR, ".results-text .duration")

    CALL_TAXI_BUTTON = (By.XPATH, "//button[contains(text(), 'Вызвать такси')]")
    BOOK_BUTTON = (By.XPATH, "//button[contains(text(), 'Забронировать')]")