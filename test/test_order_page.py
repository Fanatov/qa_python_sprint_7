import time
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
from data import Urls
from locators.order_page_locators import *
from pages.order_page import OrderPageScooter
from pages.base_page import *


class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize('name, surname, address, metro_station, phone_number, ddmmyy, days, color, comment',
                             data.FakeUser.users_try)
    def test_order_field(self, name, surname, address, metro_station, phone_number, ddmmyy, days, color, comment):
        self.driver.get(Urls.order_url)
        order_page = OrderPageScooter(self.driver)
        base_page = BasePage(self.driver)
        order_page.fill_person_info(name, surname, address, metro_station, phone_number)
        order_page.fill_rent_info(ddmmyy, days, color, comment)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.order_ready_pop_up))
        order_output = self.driver.find_element(*OrderPageLocators.order_ready_pop_up).text
        order_number = order_output.split(':')[1].split('.')[0].replace(' ', '')
        order_page.click_look_order_status()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.url_to_be(f'https://qa-scooter.praktikum-services.ru/track?t={order_number}'))
        base_page.click_scooter_logo()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/"))
        base_page.click_yandex_logo()
        expected_url = "https://dzen.ru/?redirect=true"
        redirect_url = self.driver.current_url
        assert expected_url != redirect_url
        # тестовая площадка пытается сделать кривой редирект "?yredirect=true" вместо "?redirect=true"
        # поэтому после ассерта идет переключение вкладки для следующих тестовых данных
        self.driver.switch_to.window(self.driver.window_handles[0])

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
