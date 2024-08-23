from locators.main_page_locators import MainPageLocators


class Urls:
    MAIN_PAGE_URL = f'https://qa-scooter.praktikum-services.ru/'
    ORDER_URL = f'https://qa-scooter.praktikum-services.ru/order'
    REDIRECT_URL = f'https://dzen.ru/?yredirect=true'
    NON_FINISHED_URL = f'https://qa-scooter.praktikum-services.ru/track?t='

class Answers:
    ANSWER_COST_BUTTON = f'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    ANSWER_HOW_MANY_SCOOTERS = (
        f'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто '
        f'сделать несколько заказов — один за другим.')
    ANSWER_RENT_TIME = (
        f'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени '
        f'аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в '
        f'20:30, суточная аренда закончится 9 мая в 20:30.')
    ANSWER_TODAY_ORDER = f'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    ANSWER_USE_PROLONGATION = (f'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по '
                               f'красивому номеру 1010.')
    ANSWER_CHARGER_DELIVERY = (
        f'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься '
        f'без передышек и во сне. Зарядка не понадобится.')
    ANSWER_CANCEL_ORDER = (f'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. '
                           f'Все же свои.')
    ANSWER_SCOOTER_DELIVERY_ABROAD = f'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    PARAM_QA_FIELD = [
        [MainPageLocators.question_cost_button[1], MainPageLocators.answer_cost_button[1], "Сутки — 400 рублей. Оплата курьеру — наличными или картой."],
        [MainPageLocators.question_how_many_scooters[1], MainPageLocators.answer_how_many_scooters[1], "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."],
        [MainPageLocators.question_rent_time[1], MainPageLocators.answer_rent_time[1], "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."],
        [MainPageLocators.question_today_order[1], MainPageLocators.answer_today_order[1], "Только начиная с завтрашнего дня. Но скоро станем расторопнее."],
        [MainPageLocators.question_use_prolongation[1], MainPageLocators.answer_use_prolongation[1], "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."],
        [MainPageLocators.question_charger_delivery[1], MainPageLocators.answer_charger_delivery[1], "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."],
        [MainPageLocators.question_cancel_order[1], MainPageLocators.answer_cancel_order[1], "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."],
        [MainPageLocators.question_scooter_delivery_abroad[1], MainPageLocators.answer_scooter_delivery_abroad[1], "Да, обязательно. Всем самокатов! И Москве, и Московской области."]
                      ]


class FakeUser:
    USERS_TRY = [
        ['Василий', 'Пупкин', 'Ул. Большая пупковая 4', 'Курская', '+79131543212', '03.08.2024', 'шестеро суток',
         'black', 'Комментарий'],
        ['Андрей', 'Голубкин', 'улица малая голубиная 169', 'Медведково', '+79491143714', '01.01.2025', 'сутки', 'grey',
         '']
    ]
