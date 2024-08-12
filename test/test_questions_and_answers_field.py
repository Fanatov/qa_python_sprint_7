import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import data
from selenium import webdriver
from data import Urls
from pages.base_page import BasePage


class TestQAField:
    driver = None

    @pytest.mark.parametrize('questions, answers, right_answer', data.Answers.PARAM_QA_FIELD)
    def test_questions(self, questions, answers, right_answer, driver):
        driver.get(Urls.MAIN_PAGE_URL)
        base_buttons = BasePage(driver)
        base_buttons.accept_cookies()
        driver.find_element(By.XPATH, questions).click()
        answer = driver.find_element(By.XPATH, answers).text
        assert answer in right_answer
