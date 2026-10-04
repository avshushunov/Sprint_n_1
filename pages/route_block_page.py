import allure
from pages.base_page import BasePage
from locators.route_block_locators import RouteBlockLocators


class RouteBlockPage(BasePage):

    @allure.step("Выбрать вкладку маршрута: {tab_name}")
    def select_route_tab(self, tab_name):
        tabs = {
            "Оптимальный": RouteBlockLocators.TAB_OPTIMAL,
            "Быстрый": RouteBlockLocators.TAB_FAST,
            "Свой": RouteBlockLocators.TAB_CUSTOM,
        }
        self.click(tabs[tab_name])

    @allure.step("Выбрать тип передвижения: {mode_name}")
    def select_transport_mode(self, mode_name):
        modes = {
            "Машина": RouteBlockLocators.TRANSPORT_CAR,
            "Пешком": RouteBlockLocators.TRANSPORT_WALK,
            "Такси": RouteBlockLocators.TRANSPORT_TAXI,
            "Велосипед": RouteBlockLocators.TRANSPORT_BIKE,
            "Самокат": RouteBlockLocators.TRANSPORT_SCOOTER,
            "Драйв": RouteBlockLocators.TRANSPORT_DRIVE,
        }
        self.click(modes[mode_name])

    @allure.step("Проверить, что блок выбора маршрута отображается")
    def is_route_block_displayed(self):
        self.wait_for_element(RouteBlockLocators.TYPE_PICKER)
        return self.is_displayed(RouteBlockLocators.TYPE_PICKER)

    @allure.step("Получить стоимость маршрута")
    def get_cost(self):
        self.wait_for_element(RouteBlockLocators.ROUTE_COST)
        return self.get_text(RouteBlockLocators.ROUTE_COST)

    @allure.step("Получить время маршрута")
    def get_time(self):
        self.wait_for_element(RouteBlockLocators.ROUTE_DURATION)
        return self.get_text(RouteBlockLocators.ROUTE_DURATION)

    @allure.step("Проверить, что кнопка Вызвать такси активна")
    def is_call_taxi_button_enabled(self):
        self.wait_for_element(RouteBlockLocators.CALL_TAXI_BUTTON)
        return self.is_enabled(RouteBlockLocators.CALL_TAXI_BUTTON)

    @allure.step("Проверить, что кнопка Забронировать активна")
    def is_book_button_enabled(self):
        self.wait_for_element(RouteBlockLocators.BOOK_BUTTON)
        return self.is_enabled(RouteBlockLocators.BOOK_BUTTON)

    @allure.step("Нажать кнопку Вызвать такси")
    def click_call_taxi(self):
        self.wait_for_element_clickable(RouteBlockLocators.CALL_TAXI_BUTTON)
        self.click(RouteBlockLocators.CALL_TAXI_BUTTON)

    @allure.step("Проверить, что вкладка {tab_name} активна")
    def is_tab_active(self, tab_name):
        tabs = {
            "Оптимальный": RouteBlockLocators.TAB_OPTIMAL,
            "Быстрый": RouteBlockLocators.TAB_FAST,
            "Свой": RouteBlockLocators.TAB_CUSTOM,
        }
        class_attr = self.get_attribute(tabs[tab_name], "class")
        return "active" in class_attr

    @allure.step("Проверить, что тип передвижения {mode_name} отображается")
    def is_transport_mode_displayed(self, mode_name):
        modes = {
            "Машина": RouteBlockLocators.TRANSPORT_CAR,
            "Пешком": RouteBlockLocators.TRANSPORT_WALK,
            "Такси": RouteBlockLocators.TRANSPORT_TAXI,
            "Велосипед": RouteBlockLocators.TRANSPORT_BIKE,
            "Самокат": RouteBlockLocators.TRANSPORT_SCOOTER,
            "Драйв": RouteBlockLocators.TRANSPORT_DRIVE,
        }
        self.wait_for_element(modes[mode_name])
        return self.is_displayed(modes[mode_name])

    @allure.step("Дождаться появления контейнера типов передвижения")
    def wait_for_types_container(self):
        self.wait_for_element(RouteBlockLocators.TYPES_CONTAINER)

    @allure.step("Получить текст с информацией о маршруте")
    def get_route_info_text(self):
        self.wait_for_element(RouteBlockLocators.TYPE_PICKER)
        return self.get_text(RouteBlockLocators.TYPE_PICKER)