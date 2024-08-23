import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
from data import Urls
from pages.order_page import OrderPageScooter
from pages.base_page import *


class TestOrderPage:
    driver = None

    @pytest.mark.parametrize('name, surname, address, metro_station, phone_number, ddmmyy, days, color, comment',
                             data.FakeUser.USERS_TRY)
    def test_order_field(self, name, surname, address, metro_station, phone_number, ddmmyy, days, color, comment, driver):
        driver.get(Urls.ORDER_URL)
        order_page = OrderPageScooter(driver)
        order_page.accept_cookies()
        order_page.fill_person_info(name, surname, address, metro_station, phone_number)
        order_page.fill_rent_info(ddmmyy, days, color, comment)
        order_page.wait_for_element(OrderPageLocators.order_ready_pop_up)
        order_number = order_page.get_order_number(OrderPageLocators.order_ready_pop_up)
        order_page.click_look_order_status()
        order_page.wait_for_url_element(data.Urls.NON_FINISHED_URL+f'{order_number}')
        order_page.click_scooter_logo()
        order_page.wait_for_url_element(Urls.MAIN_PAGE_URL)
        order_page.click_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        order_page.wait_for_url_element(Urls.REDIRECT_URL)
        expected_url = Urls.REDIRECT_URL
        redirect_url = driver.current_url
        driver.switch_to.window(driver.window_handles[0])
        assert redirect_url in expected_url

