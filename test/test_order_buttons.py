import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Urls
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPageScooter


class TestButtons:
    driver = None

    def test_big_order_button(self, driver):
        driver.get(Urls.MAIN_PAGE_URL)
        login_page = MainPageScooter(driver)
        login_page.accept_cookies()
        login_page.click_order_big_button()
        login_page.wait_for_element(OrderPageLocators.order_title)
        assert login_page.driver.current_url == Urls.ORDER_URL

    def test_small_order_button(self, driver):
        driver.get(Urls.MAIN_PAGE_URL)
        login_page = MainPageScooter(driver)
        login_page.accept_cookies()
        login_page.click_order_small_button()
        login_page.wait_for_element(OrderPageLocators.order_title)
        assert login_page.driver.current_url == Urls.ORDER_URL
