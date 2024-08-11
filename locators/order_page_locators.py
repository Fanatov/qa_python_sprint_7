from selenium.webdriver.common.by import By


class OrderPageLocators:
    order_title = [By.XPATH, "//div[contains(@class,'Order_Header')]"]
    proceed_button = [By.XPATH, "//button[.='Далее']"]
    name_field = [By.XPATH, "//input[@placeholder='* Имя']"]
    surname_field = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    address_field = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro_station_list_field = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    phone_number_field = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    ddmmyy_field = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    rent_period_field = [By.XPATH, "//div[@class='Dropdown-control']"]
    scooter_color_black_checkbox = [By.XPATH, "/html//input[@id='black']"]
    scooter_color_grey_checkbox = [By.XPATH, "/html//input[@id='grey']"]
    comment_section = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    go_back_button = [By.XPATH, "//button[text()='Назад']"]
    make_order_button = [By.XPATH, "//button[(contains(@class,'Middle')) and not (contains(@class,'Inverted'))]"]
    order_agreed = [By.XPATH, "//button[contains(text(),'Да')]"]
    order_denied = [By.XPATH, "//button[contains(text(),'Нет')]"]
    track_order_button = [By.XPATH, "//button[contains(text(),'Посмотреть статус')]"]
    order_ready_pop_up = [By.XPATH, "//div[contains(text(),'Заказ оформлен')]"]
    title_about_rent = [By.XPATH, "//div[text()='Про аренду']"]

