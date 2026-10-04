import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.taxi_order_locators import TaxiOrderLocators


class TaxiOrderPage(BasePage):

    @allure.step("Проверить, что форма заказа такси отображается")
    def is_tariff_picker_displayed(self):
        self.wait_for_element(TaxiOrderLocators.TARIFF_PICKER)
        return self.is_displayed(TaxiOrderLocators.TARIFF_PICKER)

    @allure.step("Проверить, что тариф отображается: {tariff_name}")
    def is_tariff_displayed(self, tariff_name):
        locator = (
            By.XPATH,
            TaxiOrderLocators.TARIFF_CARD_BY_TITLE.format(tariff_name)
        )
        self.wait_for_element(locator)
        return self.is_displayed(locator)

    @allure.step("Проверить, что тариф {tariff_name} активен")
    def is_tariff_active(self, tariff_name):
        locator = (
            By.XPATH,
            TaxiOrderLocators.TARIFF_CARD_BY_TITLE.format(tariff_name)
        )
        class_attr = self.get_attribute(locator, "class")
        return "active" in class_attr

    @allure.step("Выбрать тариф: {tariff_name}")
    def select_tariff(self, tariff_name):
        locator = (
            By.XPATH,
            TaxiOrderLocators.TARIFF_CARD_BY_TITLE.format(tariff_name)
        )
        self.click(locator)

    @allure.step("Получить стоимость выбранного тарифа {tariff_name}")
    def get_tariff_price(self, tariff_name):
        locator = (
            By.XPATH,
            TaxiOrderLocators.TARIFF_PRICE_BY_TITLE.format(tariff_name)
        )
        self.wait_for_element(locator)
        return self.get_text(locator)

    @allure.step("Навести на иконку информации тарифа {tariff_name}")
    def hover_tariff_info(self, tariff_name):
        card_locator = (
            By.XPATH,
            TaxiOrderLocators.TARIFF_CARD_BY_TITLE.format(tariff_name)
        )
        info_locator = (
            By.XPATH,
            TaxiOrderLocators.TARIFF_INFO_BUTTON_BY_TITLE.format(tariff_name)
        )
        self.click(card_locator)
        self.hover(info_locator)

    @allure.step("Получить описание тарифа из всплывающего окна")
    def get_tariff_tooltip_text(self):
        self.wait_for_element(TaxiOrderLocators.TARIFF_TOOLTIP_VISIBLE)
        return self.get_text(TaxiOrderLocators.TARIFF_TOOLTIP_VISIBLE)

    @allure.step("Включить чекбокс Столик для ноутбука")
    def enable_laptop_table(self):
        self.click_js(TaxiOrderLocators.REQUIREMENTS_HEAD)
        self.wait_for_element(TaxiOrderLocators.LAPTOP_CHECKBOX)
        self.click(TaxiOrderLocators.LAPTOP_CHECKBOX)
        self.click_js(TaxiOrderLocators.REQUIREMENTS_HEAD)

    @allure.step("Нажать кнопку Ввести номер и заказать")
    def click_order_button(self):
        self.click(TaxiOrderLocators.ORDER_BUTTON)

    @allure.step("Дождаться появления окна Поиск машины")
    def wait_for_car_search(self):
        self.wait_for_element(TaxiOrderLocators.SEARCH_CAR_HEADER, timeout=30)

    @allure.step("Проверить, что таймер обратного отсчета отображается")
    def is_search_timer_displayed(self):
        self.wait_for_element(TaxiOrderLocators.SEARCH_TIMER)
        return self.is_displayed(TaxiOrderLocators.SEARCH_TIMER)

    @allure.step("Дождаться окончания поиска и появления окна завершенного заказа")
    def wait_for_order_complete(self):
        self.wait_for_element(TaxiOrderLocators.ORDER_COMPLETE_HEADER, timeout=120)

    @allure.step("Проверить, что окно завершенного заказа отображается")
    def is_order_complete_displayed(self):
        return self.is_displayed(TaxiOrderLocators.ORDER_COMPLETE_HEADER)

    @allure.step("Проверить, что номер автомобиля отображается")
    def is_car_number_displayed(self):
        self.wait_for_element(TaxiOrderLocators.CAR_NUMBER)
        return self.is_displayed(TaxiOrderLocators.CAR_NUMBER)

    @allure.step("Проверить, что картинка тарифа отображается")
    def is_car_picture_displayed(self):
        self.wait_for_element(TaxiOrderLocators.CAR_PHOTO)
        return self.is_displayed(TaxiOrderLocators.CAR_PHOTO)

    @allure.step("Проверить, что имя водителя отображается")
    def is_driver_name_displayed(self):
        self.wait_for_element(TaxiOrderLocators.DRIVER_NAME)
        return self.is_displayed(TaxiOrderLocators.DRIVER_NAME)

    @allure.step("Проверить, что фото водителя отображается")
    def is_driver_photo_displayed(self):
        self.wait_for_element(TaxiOrderLocators.DRIVER_PHOTO)
        return self.is_displayed(TaxiOrderLocators.DRIVER_PHOTO)

    @allure.step("Проверить, что рейтинг водителя отображается")
    def is_driver_rating_displayed(self):
        self.wait_for_element(TaxiOrderLocators.DRIVER_RATING)
        return self.is_displayed(TaxiOrderLocators.DRIVER_RATING)

    @allure.step("Нажать кнопку Детали")
    def click_details(self):
        self.click(TaxiOrderLocators.DETAILS_BUTTON)

    @allure.step("Получить стоимость из окна Детали")
    def get_details_cost(self):
        self.wait_for_element(TaxiOrderLocators.DETAILS_COST)
        return self.get_text(TaxiOrderLocators.DETAILS_COST)

    @allure.step("Нажать кнопку Отменить")
    def click_cancel(self):
        self.click(TaxiOrderLocators.CANCEL_BUTTON)

    @allure.step("Проверить, что окно заказа закрылось")
    def is_order_window_closed(self):
        return self.wait_for_element_invisible(TaxiOrderLocators.ORDER_BODY)

    @allure.step("Проверить, что поля заказа отображаются")
    def are_order_fields_displayed(self):
        self.wait_for_element(TaxiOrderLocators.PHONE_FIELD)
        self.wait_for_element(TaxiOrderLocators.PAYMENT_VALUE)
        self.wait_for_element(TaxiOrderLocators.COMMENT_FIELD)
        self.wait_for_element(TaxiOrderLocators.REQUIREMENTS_HEAD)
        phone = self.is_displayed(TaxiOrderLocators.PHONE_FIELD)
        payment = self.is_displayed(TaxiOrderLocators.PAYMENT_VALUE)
        comment = self.is_displayed(TaxiOrderLocators.COMMENT_FIELD)
        requirements = self.is_displayed(TaxiOrderLocators.REQUIREMENTS_HEAD)
        return phone and payment and comment and requirements