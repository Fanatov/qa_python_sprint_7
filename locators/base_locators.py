from selenium.webdriver.common.by import By


class BaseLocators:
    cookie_button = [By.ID, "rcc-confirm-button"]
    scooter_logo = [By.XPATH, "//img[@alt='Scooter']"]
    yandex_logo = [By.XPATH, "//img[@alt='Yandex']"]