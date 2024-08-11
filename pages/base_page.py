from locators.base_locators import BaseLocators


# Общий класс страниц
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        self.driver.find_element(*BaseLocators.cookie_button).click()

    def scroll_to_some_element(self, some_element):
        element = self.driver.find_element(*some_element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_scooter_logo(self):
        self.driver.find_element(*BaseLocators.scooter_logo).click()

    def click_yandex_logo(self):
        self.driver.find_element(*BaseLocators.yandex_logo).click()
