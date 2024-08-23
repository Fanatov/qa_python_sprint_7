from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


# Класс страницы авторизации
class OrderPageScooter(BasePage):

    def click_proceed_button(self):
        self.driver.find_element(*OrderPageLocators.proceed_button).click()

    def name_input(self, name):
        self.driver.find_element(*OrderPageLocators.name_field).send_keys(name)

    def name_input_click(self):
        self.driver.find_element(*OrderPageLocators.name_field).click()

    def surname_input(self, surname):
        self.driver.find_element(*OrderPageLocators.surname_field).send_keys(surname)

    def address_input(self, address):
        self.driver.find_element(*OrderPageLocators.address_field).send_keys(address)

    def metro_station_input(self, station):
        self.driver.find_element(*OrderPageLocators.metro_station_list_field).click()
        self.driver.find_element(By.XPATH, f"//div[.='{station}']").click()

    def phone_number_input(self, phone_number):
        self.driver.find_element(*OrderPageLocators.phone_number_field).send_keys(phone_number)

    def click_make_order_button(self):
        self.driver.find_element(*OrderPageLocators.make_order_button).click()

    def ddmmyy_field_input(self, ddmmyy):
        self.driver.find_element(*OrderPageLocators.ddmmyy_field).send_keys(ddmmyy)

    def rent_period_field_input(self, days):
        self.driver.find_element(*OrderPageLocators.rent_period_field).click()
        self.driver.find_element(By.XPATH, f"//div[contains(text(),'{days}')]").click()

    def comment_section_input(self, commentary):
        self.driver.find_element(*OrderPageLocators.comment_section).send_keys(commentary)

    def title_about_rent_click(self):
        self.driver.find_element(*OrderPageLocators.title_about_rent).click()

    def click_scooter_color_checkbox(self, color):
        self.driver.find_element(By.XPATH, f"/html//input[@id='{color}']").click()

    def click_confirm_button(self):
        self.driver.find_element(*OrderPageLocators.order_agreed).click()

    def click_deny_button(self):
        self.driver.find_element(*OrderPageLocators.order_denied).click()

    def click_look_order_status(self):
        self.driver.find_element(*OrderPageLocators.track_order_button).click()

    def fill_person_info(self, name, surname, address, metro_station, phone_number):
        self.name_input(name)
        self.surname_input(surname)
        self.address_input(address)
        self.metro_station_input(metro_station)
        self.phone_number_input(phone_number)
        self.click_proceed_button()
        self.click_make_order_button()

    def fill_rent_info(self, ddmmyy, days, color, comment):
        self.ddmmyy_field_input(ddmmyy)
        self.title_about_rent_click()
        self.rent_period_field_input(days)
        self.click_scooter_color_checkbox(color)
        self.comment_section_input(comment)
        self.click_make_order_button()
        self.click_confirm_button()

    def get_order_number(self, locator):
        self.wait_for_element(locator)
        order_num = self.driver.find_element(*locator).text.split(':')[1].split('.')[0].replace(' ', '')
        return order_num
