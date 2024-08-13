from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


# Класс главной авторизации
class MainPageScooter(BasePage):

    def click_order_small_button(self):
        self.driver.find_element(*MainPageLocators.small_order_button).click()

    def click_order_big_button(self):
        self.driver.find_element(*MainPageLocators.big_order_button).click()

    def click_question_cost_button(self):
        self.driver.find_element(*MainPageLocators.question_cost_button).click()

    def click_question_how_many_scooters(self):
        self.driver.find_element(*MainPageLocators.question_how_many_scooters).click()

    def click_question_rent_time(self):
        self.driver.find_element(*MainPageLocators.question_rent_time).click()

    def click_question_today_order(self):
        self.driver.find_element(*MainPageLocators.question_today_order).click()

    def click_question_use_prolongation(self):
        self.driver.find_element(*MainPageLocators.question_use_prolongation).click()

    def click_question_charger_delivery(self):
        self.driver.find_element(*MainPageLocators.question_charger_delivery).click()

    def click_question_cancel_order(self):
        self.driver.find_element(*MainPageLocators.question_cancel_order).click()

    def click_question_scooter_delivery_abroad(self):
        self.driver.find_element(*MainPageLocators.question_scooter_delivery_abroad).click()
