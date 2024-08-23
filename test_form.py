from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from automation_practice_form import AutomatonPracticeForm
from time import sleep

class Test:
    @pytest.mark.practiceForm
    @allure.feature('Practice form')
    @allure.story('Practice form')
    def test_practice_form(self, browser):
        test_page = AutomatonPracticeForm(browser)
        test_page.go_to_site()
        test_page.set_firstname("Алексей")
        test_page.set_lastname("Кузнецов")
        test_page.set_email("horizondd73@gmail.com")
        test_page.set_gender('2') # 1 - male, 2 - female, другое значение - other
        test_page.set_mobile("1234567890")
        test_page.open_calendar()
        test_page.set_month('2') # № месяца по порядку 0 - январь, 11 - декабрь
        test_page.set_year('1994')
        test_page.set_day(18)
        test_page.set_subject("eng")
        test_page.set_picture("C:/Users/horiz/OneDrive/Desktop/sdet-main/1.png") # перед запуском указать корректный путь
        test_page.set_address("Ульяновская область, город Димитровград, Алтайская ул., д. 1")
        test_page.set_state()
        test_page.set_city()
        test_page.click_submit()

# pytest -s -v --alluredir results
# allure serve results
