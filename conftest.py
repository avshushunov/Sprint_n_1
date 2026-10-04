import pytest
from selenium import webdriver
from constants import URL
from data.test_data import ADDRESS_FROM, ADDRESS_TO
from pages.main_page import MainPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.wait_for_map_loaded()
    return page


@pytest.fixture
def route_page(main_page):
    main_page.fill_from_address(ADDRESS_FROM)
    main_page.select_first_suggestion_from()
    main_page.fill_to_address(ADDRESS_TO)
    main_page.select_first_suggestion_to()
    return main_page