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
        base_page = BasePage(driver)
        base_page.accept_cookies()
        order_page.fill_person_info(name, surname, address, metro_station, phone_number)
        order_page.fill_rent_info(ddmmyy, days, color, comment)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.order_ready_pop_up))
        order_output = driver.find_element(*OrderPageLocators.order_ready_pop_up).text
        order_number = order_output.split(':')[1].split('.')[0].replace(' ', '')
        order_page.click_look_order_status()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(f'https://qa-scooter.praktikum-services.ru/track?t={order_number}'))
        base_page.click_scooter_logo()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(Urls.MAIN_PAGE_URL))
        base_page.click_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(Urls.REDIRECT_URL))
        expected_url = Urls.REDIRECT_URL
        redirect_url = driver.current_url
        driver.switch_to.window(driver.window_handles[0])
        assert redirect_url in expected_url

