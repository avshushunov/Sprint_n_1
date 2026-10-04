import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Ввести адрес в поле Откуда: {address}")
    def fill_from_address(self, address):
        self.send_keys(MainPageLocators.ADDRESS_INPUT_FROM, address)

    @allure.step("Ввести адрес в поле Куда: {address}")
    def fill_to_address(self, address):
        self.send_keys(MainPageLocators.ADDRESS_INPUT_TO, address)

    @allure.step("Выбрать первый адрес из подсказок для поля Откуда")
    def select_first_suggestion_from(self):
        element = self.find_element(MainPageLocators.ADDRESS_INPUT_FROM)
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    @allure.step("Выбрать первый адрес из подсказок для поля Куда")
    def select_first_suggestion_to(self):
        element = self.find_element(MainPageLocators.ADDRESS_INPUT_TO)
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    @allure.step("Проверить, что первая точка маршрута отображается на карте")
    def is_route_point_a_displayed(self):
        self.wait_for_element(MainPageLocators.ROUTE_POINT_A, timeout=15)
        return self.is_displayed(MainPageLocators.ROUTE_POINT_A)

    @allure.step("Проверить, что вторая точка маршрута отображается на карте")
    def is_route_point_b_displayed(self):
        self.wait_for_element(MainPageLocators.ROUTE_POINT_B, timeout=15)
        return self.is_displayed(MainPageLocators.ROUTE_POINT_B)

    @allure.step("Дождаться загрузки карты")
    def wait_for_map_loaded(self):
        self.wait_for_element(MainPageLocators.MAP)