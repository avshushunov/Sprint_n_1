import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator):
        self.find_element(locator).click()

    @allure.step("Ввести '{text}' в поле {locator}")
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Проверить, что элемент {locator} отображается")
    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    @allure.step("Проверить, что элемент {locator} активен")
    def is_enabled(self, locator):
        return self.find_element(locator).is_enabled()

    @allure.step("Получить атрибут {attribute} элемента {locator}")
    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    @allure.step("Ожидание появления элемента {locator}")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание кликабельности элемента {locator}")
    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Ожидание исчезновения элемента {locator}")
    def wait_for_element_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Навести курсор на элемент {locator}")
    def hover(self, locator):
        element = self.find_element(locator)
        action = ActionChains(self.driver).move_to_element(element)
        action.perform()

    @allure.step("Кликнуть по элементу через JavaScript {locator}")
    def click_js(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)