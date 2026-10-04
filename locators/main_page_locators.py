from selenium.webdriver.common.by import By

class MainPageLocators:
    ADDRESS_INPUT_FROM = (By.ID, "from")
    ADDRESS_INPUT_TO = (By.ID, "to")
    MAP = (By.ID, "map")
    ROUTE_POINT_A = (By.XPATH, "//*[contains(@class, 'route-pin__label-a')]")
    ROUTE_POINT_B = (By.XPATH, "//*[contains(@class, 'route-pin__label-b')]")