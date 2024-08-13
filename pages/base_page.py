from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_locators import BaseLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


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

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_url_element(self, url):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url))

