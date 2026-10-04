import allure
import pytest
from pages.route_block_page import RouteBlockPage
from pages.taxi_order_page import TaxiOrderPage
from data.test_data import TAXI_TARIFFS


@allure.epic("Заказ тарифа Такси")
class TestTaxiOrder:

    @allure.title("Открывается форма заказа со всеми 6 тарифами, один из них активный")
    def test_taxi_order_form_opens_with_active_tariff(self, driver, route_page):
        route_block = RouteBlockPage(driver)
        taxi_order = TaxiOrderPage(driver)

        route_block.is_route_block_displayed()
        route_block.select_route_tab("Быстрый")
        route_block.click_call_taxi()

        assert taxi_order.is_tariff_picker_displayed()
        assert taxi_order.is_tariff_active("Рабочий")

    @allure.title("В форме заказа отображается тариф")
    @pytest.mark.parametrize("tariff_name", TAXI_TARIFFS)
    def test_tariff_displayed(self, driver, route_page, tariff_name):
        route_block = RouteBlockPage(driver)
        taxi_order = TaxiOrderPage(driver)

        route_block.is_route_block_displayed()
        route_block.select_route_tab("Быстрый")
        route_block.click_call_taxi()

        assert taxi_order.is_tariff_displayed(tariff_name)

    @allure.title("При наведении на иконку i отображается описание тарифа соответствующее ТЗ")
    @pytest.mark.parametrize("tariff_name, expected_description", [
        pytest.param("Рабочий", TAXI_TARIFFS["Рабочий"]),
        pytest.param("Сонный", TAXI_TARIFFS["Сонный"], marks=pytest.mark.xfail(reason="Описание Сонного перепутано с Разговорчивым")),
        pytest.param("Отпускной", TAXI_TARIFFS["Отпускной"]),
        pytest.param("Разговорчивый", TAXI_TARIFFS["Разговорчивый"], marks=pytest.mark.xfail(reason="Описание Разговорчивого перепутано с Сонным")),
        pytest.param("Утешительный", TAXI_TARIFFS["Утешительный"]),
        pytest.param("Глянцевый", TAXI_TARIFFS["Глянцевый"]),
    ])
    def test_tariff_info_hover_shows_description(self, driver, route_page, tariff_name, expected_description):
        route_block = RouteBlockPage(driver)
        taxi_order = TaxiOrderPage(driver)

        route_block.is_route_block_displayed()
        route_block.select_route_tab("Быстрый")
        route_block.click_call_taxi()

        taxi_order.hover_tariff_info(tariff_name)
        actual_description = taxi_order.get_tariff_tooltip_text()
        assert expected_description in actual_description

    @allure.title("Под тарифами отображается блок с полями Телефон, Способ оплаты, Комментарий водителю, Требования к заказу")
    def test_order_form_fields_displayed(self, driver, route_page):
        route_block = RouteBlockPage(driver)
        taxi_order = TaxiOrderPage(driver)

        route_block.is_route_block_displayed()
        route_block.select_route_tab("Быстрый")
        route_block.click_call_taxi()

        assert taxi_order.are_order_fields_displayed()

    @allure.title("После нажатия кнопки заказа появляется окно Поиск машины с таймером")
    def test_order_shows_car_search(self, driver, route_page):
        route_block = RouteBlockPage(driver)
        taxi_order = TaxiOrderPage(driver)

        route_block.is_route_block_displayed()
        route_block.select_route_tab("Быстрый")
        route_block.click_call_taxi()

        taxi_order.select_tariff("Рабочий")
        taxi_order.enable_laptop_table()
        taxi_order.click_order_button()

        taxi_order.wait_for_car_search()
        assert taxi_order.is_search_timer_displayed()

    @allure.title("После окончания поиска отображается окно совершенного заказа с данными водителя")
    def test_completed_order_shows_driver_info(self, driver, route_page):
        route_block = RouteBlockPage(driver)
        taxi_order = TaxiOrderPage(driver)

        route_block.is_route_block_displayed()
        route_block.select_route_tab("Быстрый")
        route_block.click_call_taxi()

        taxi_order.select_tariff("Рабочий")
        taxi_order.enable_laptop_table()
        taxi_order.click_order_button()

        taxi_order.wait_for_order_complete()
        assert taxi_order.is_order_complete_displayed()
        assert taxi_order.is_car_number_displayed()
        assert taxi_order.is_car_picture_displayed()
        assert taxi_order.is_driver_name_displayed()
        assert taxi_order.is_driver_photo_displayed()
        assert taxi_order.is_driver_rating_displayed()

    @allure.title("Стоимость в деталях совпадает с выбранным тарифом")
    def test_details_cost_matches_tariff(self, driver, route_page):
        route_block = RouteBlockPage(driver)
        taxi_order = TaxiOrderPage(driver)

        route_block.is_route_block_displayed()
        route_block.select_route_tab("Быстрый")
        route_block.click_call_taxi()

        taxi_order.select_tariff("Рабочий")
        saved_cost = taxi_order.get_tariff_price("Рабочий")
        saved_cost_value = saved_cost.split(" ")[0]

        taxi_order.enable_laptop_table()
        taxi_order.click_order_button()

        taxi_order.wait_for_order_complete()
        taxi_order.click_details()
        details_cost = taxi_order.get_details_cost()
        assert saved_cost_value in details_cost

    @allure.title("Кнопка Отмена закрывает окно заказа")
    def test_cancel_closes_order_window(self, driver, route_page):
        route_block = RouteBlockPage(driver)
        taxi_order = TaxiOrderPage(driver)

        route_block.is_route_block_displayed()
        route_block.select_route_tab("Быстрый")
        route_block.click_call_taxi()

        taxi_order.select_tariff("Рабочий")
        taxi_order.enable_laptop_table()
        taxi_order.click_order_button()

        taxi_order.wait_for_order_complete()
        taxi_order.click_cancel()
        assert taxi_order.is_order_window_closed()