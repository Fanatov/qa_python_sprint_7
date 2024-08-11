from selenium.webdriver.common.by import By


class MainPageLocators:
    small_order_button = [By.XPATH, "//button[contains(@class,'Button_Button')]"]

    big_order_button = [By.XPATH, "//div[contains(@class,'Home_FinishButton')]"]

    question_cost_button = [By.XPATH, "(//div[@id='accordion__heading-0'])[1]"]
    answer_cost_button = [By.XPATH, "(//div[@id='accordion__panel-0'])[1]"]

    question_how_many_scooters = [By.XPATH, "(//div[@id='accordion__heading-1'])[1]"]
    answer_how_many_scooters = [By.XPATH, "(//div[@id='accordion__panel-1'])[1]"]

    question_rent_time = [By.XPATH, "(//div[@id='accordion__heading-2'])[1]"]
    answer_rent_time = [By.XPATH, "(//div[@id='accordion__panel-2'])[1]"]

    question_today_order = [By.XPATH, "(//div[@id='accordion__heading-3'])[1]"]
    answer_today_order = [By.XPATH, "(//div[@id='accordion__panel-3'])[1]"]

    question_use_prolongation = [By.XPATH, "(//div[@id='accordion__heading-4'])[1]"]
    answer_use_prolongation = [By.XPATH, "(//div[@id='accordion__panel-4'])[1]"]

    question_charger_delivery = [By.XPATH, "(//div[@id='accordion__heading-5'])[1]"]
    answer_charger_delivery = [By.XPATH, "(//div[@id='accordion__panel-5'])[1]"]

    question_cancel_order = [By.XPATH, "(//div[@id='accordion__heading-6'])[1]"]
    answer_cancel_order = [By.XPATH, "(//div[@id='accordion__panel-6'])[1]"]

    question_scooter_delivery_abroad = [By.XPATH, "(//div[@id='accordion__heading-7'])[1]"]
    answer_scooter_delivery_abroad = [By.XPATH, "(//div[@id='accordion__panel-7'])[1]"]

    questions_main_title = [By.XPATH, "//div[contains(@class,'Home_SubHeader')]"]
