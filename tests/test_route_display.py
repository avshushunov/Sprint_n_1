import allure
from data.test_data import ADDRESS_FROM, ADDRESS_TO


@allure.epic("Отрисовка маршрута")
class TestRouteDisplay:

    @allure.title("При вводе двух разных адресов на карте отображаются две точки маршрута")
    def test_route_points_displayed_on_map(self, main_page):
        main_page.fill_from_address(ADDRESS_FROM)
        main_page.select_first_suggestion_from()
        main_page.fill_to_address(ADDRESS_TO)
        main_page.select_first_suggestion_to()

        assert main_page.is_route_point_a_displayed()
        assert main_page.is_route_point_b_displayed()