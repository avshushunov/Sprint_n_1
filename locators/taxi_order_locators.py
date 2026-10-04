from selenium.webdriver.common.by import By

class TaxiOrderLocators:
    TARIFF_PICKER = (By.CSS_SELECTOR, ".tariff-picker")
    TARIFF_CARD_BY_TITLE = "//div[@class='tcard-title' and text()='{}']/parent::div"
    TARIFF_PRICE_BY_TITLE = "//div[@class='tcard-title' and text()='{}']/parent::div//div[@class='tcard-price']"
    TARIFF_INFO_BUTTON_BY_TITLE = "//div[@class='tcard-title' and text()='{}']/parent::div//button[contains(@class, 'tcard-i')]"
    TARIFF_TOOLTIP_VISIBLE = (By.CSS_SELECTOR, "[class*='tooltip'][class*='show']")

    PHONE_FIELD = (By.XPATH, "//div[contains(@class, 'np-text') and text()='Телефон']")
    PAYMENT_VALUE = (By.XPATH, "//div[contains(@class, 'pp-value-text') and text()='Наличные']")
    COMMENT_FIELD = (By.XPATH, "//label[contains(text(), 'Комментарий')]")
    REQUIREMENTS_HEAD = (By.CSS_SELECTOR, ".reqs-head")

    LAPTOP_CHECKBOX = (By.CSS_SELECTOR, ".r-sw-label")

    ORDER_BUTTON = (By.CSS_SELECTOR, ".smart-button")

    SEARCH_CAR_HEADER = (By.XPATH, "//*[contains(text(), 'Поиск машины')]")
    SEARCH_TIMER = (By.CSS_SELECTOR, ".order-header-time")
    ORDER_COMPLETE_HEADER = (By.XPATH, "//div[contains(@class, 'order-header-title') and contains(., 'приедет')]")
    ORDER_BODY = (By.CSS_SELECTOR, ".order-body")
    CAR_NUMBER = (By.CSS_SELECTOR, ".order-number .number")
    CAR_PHOTO = (By.CSS_SELECTOR, ".order-number img")
    DRIVER_NAME = (By.XPATH, "//div[contains(@class, 'order-btn-rating')]/parent::div/following-sibling::div")
    DRIVER_PHOTO = (By.XPATH, "//div[contains(@class, 'order-btn-rating')]/parent::div/img")
    DRIVER_RATING = (By.CSS_SELECTOR, ".order-btn-rating")
    CANCEL_BUTTON = (By.XPATH, "//div[text()='Отменить']/preceding-sibling::button")
    DETAILS_BUTTON = (By.XPATH, "//div[text()='Детали']/preceding-sibling::button")

    DETAILS_COST = (By.XPATH, "//div[contains(@class, 'o-d-sh') and contains(., 'Стоимость')]")