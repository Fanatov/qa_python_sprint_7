from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Urls
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPageScooter


class TestButtons:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_big_order_button(self):
        self.driver.get(Urls.main_page_url)
        base_button = BasePage(self.driver)
        base_button.accept_cookies()
        login_page = MainPageScooter(self.driver)
        login_page.click_order_big_button()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.order_title))
        assert login_page.driver.current_url == Urls.order_url

    def test_small_order_button(self):
        self.driver.get(Urls.main_page_url)
        login_page = MainPageScooter(self.driver)
        login_page.click_order_small_button()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.order_title))
        assert login_page.driver.current_url == Urls.order_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
