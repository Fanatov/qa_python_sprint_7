import data
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPageScooter
from selenium import webdriver
from data import Urls
from pages.base_page import BasePage


class TestQAField:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_question_cost_button(self):
        self.driver.get(Urls.main_page_url)
        base_buttons = BasePage(self.driver)
        base_buttons.accept_cookies()
        login_page = MainPageScooter(self.driver)
        login_page.click_question_cost_button()
        answer = self.driver.find_element(*MainPageLocators.answer_cost_button).text
        assert answer in data.Answers.answer_cost_button

    def test_question_how_many_scooters(self):
        self.driver.get(Urls.main_page_url)
        login_page = MainPageScooter(self.driver)
        login_page.click_question_how_many_scooters()
        answer = self.driver.find_element(*MainPageLocators.answer_how_many_scooters).text
        assert answer in data.Answers.answer_how_many_scooters

    def test_question_rent_time(self):
        self.driver.get(Urls.main_page_url)
        login_page = MainPageScooter(self.driver)
        login_page.click_question_rent_time()
        answer = self.driver.find_element(*MainPageLocators.answer_rent_time).text
        assert answer in data.Answers.answer_rent_time

    def test_question_today_order(self):
        self.driver.get(Urls.main_page_url)
        login_page = MainPageScooter(self.driver)
        login_page.click_question_today_order()
        answer = self.driver.find_element(*MainPageLocators.answer_today_order).text
        assert answer in data.Answers.answer_today_order

    def test_question_use_prolongation(self):
        self.driver.get(Urls.main_page_url)
        login_page = MainPageScooter(self.driver)
        login_page.click_question_use_prolongation()
        answer = self.driver.find_element(*MainPageLocators.answer_use_prolongation).text
        assert answer in data.Answers.answer_use_prolongation

    def test_question_charger_delivery(self):
        self.driver.get(Urls.main_page_url)
        login_page = MainPageScooter(self.driver)
        login_page.click_question_charger_delivery()
        answer = self.driver.find_element(*MainPageLocators.answer_charger_delivery).text
        assert answer in data.Answers.answer_charger_delivery

    def test_question_cancel_order(self):
        self.driver.get(Urls.main_page_url)
        login_page = MainPageScooter(self.driver)
        login_page.click_question_cancel_order()
        answer = self.driver.find_element(*MainPageLocators.answer_cancel_order).text
        assert answer in data.Answers.answer_cancel_order

    def test_question_scooter_delivery_abroad(self):
        self.driver.get(Urls.main_page_url)
        login_page = MainPageScooter(self.driver)
        login_page.click_question_scooter_delivery_abroad()
        answer = self.driver.find_element(*MainPageLocators.answer_scooter_delivery_abroad).text
        assert answer in data.Answers.answer_scooter_delivery_abroad

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
