import allure
import pytest
from pages.route_block_page import RouteBlockPage
from data.test_data import TRANSPORT_TYPES


@allure.epic("Подготовка к заказу такси")
class TestTaxiPreparation:

    @allure.title("При переключении между видами маршрута Оптимальный/Быстрый происходит смена активного таба и пересчет времени и стоимости")
    def test_switch_route_tab_changes_time_and_cost(self, driver, route_page):
        route_block = RouteBlockPage(driver)

        route_block.is_route_block_displayed()
        route_block.select_route_tab("Быстрый")
        time_fast = route_block.get_time()
        cost_fast = route_block.get_cost()

        route_block.select_route_tab("Оптимальный")
        time_optimal = route_block.get_time()
        cost_optimal = route_block.get_cost()

        assert route_block.is_tab_active("Оптимальный")
        assert time_fast != time_optimal or cost_fast != cost_optimal

    @allure.title("При переключении на вид маршрута Свой активен тип передвижения")
    @pytest.mark.parametrize("mode", TRANSPORT_TYPES)
    def test_custom_tab_activates_transport_mode(self, driver, route_page, mode):
        route_block = RouteBlockPage(driver)

        route_block.is_route_block_displayed()
        route_block.select_route_tab("Свой")
        route_block.wait_for_types_container()

        assert route_block.is_tab_active("Свой")
        assert route_block.is_transport_mode_displayed(mode)

    @allure.title("При выборе вида маршрута Быстрый активна кнопка Вызвать такси")
    def test_fast_tab_shows_call_taxi_button(self, driver, route_page):
        route_block = RouteBlockPage(driver)

        route_block.is_route_block_displayed()
        route_block.select_route_tab("Быстрый")

        assert route_block.is_call_taxi_button_enabled()

    @allure.title("При выборе вида маршрута Свой и типа Драйв активна кнопка Забронировать")
    def test_custom_drive_shows_book_button(self, driver, route_page):
        route_block = RouteBlockPage(driver)

        route_block.is_route_block_displayed()
        route_block.select_route_tab("Свой")
        route_block.select_transport_mode("Драйв")

        assert route_block.is_book_button_enabled()