import allure
from pages.main_page import MainPage
from pages.route_block_page import RouteBlockPage
from data.test_data import ADDRESS_FROM


@allure.epic("Отрисовка блока с выбором маршрута")
class TestRouteSelection:

    @allure.title("При вводе двух разных адресов отображается блок с выбором маршрута")
    def test_route_block_displayed_different_addresses(self, driver, route_page):
        route_block = RouteBlockPage(driver)

        assert route_block.is_route_block_displayed()

    @allure.title("При вводе одинакового адреса отображается блок с текстом 'Авто Бесплатно В пути 0 мин.'")
    def test_route_block_same_address_shows_info(self, driver):
        main_page = MainPage(driver)
        route_block = RouteBlockPage(driver)

        main_page.wait_for_map_loaded()
        main_page.fill_from_address(ADDRESS_FROM)
        main_page.select_first_suggestion_from()
        main_page.fill_to_address(ADDRESS_FROM)
        main_page.select_first_suggestion_to()

        assert route_block.is_route_block_displayed()
        route_info = route_block.get_route_info_text()
        assert "Авто Бесплатно" in route_info
        assert "В пути 0 мин." in route_info