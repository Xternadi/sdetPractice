from base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
import allure

class Locators:
    first_name = (By.ID, "firstName")
    last_name = (By.ID, "lastName")
    email = (By.ID, "userEmail")
    gender_male = (By.XPATH, "//label[contains(text(), 'Male')]")
    gender_female = (By.XPATH, "//label[contains(text(), 'Female')]")
    gender_other = (By.XPATH, "//label[contains(text(), 'Other')]")
    mobile = (By.ID, "userNumber")
    date = (By.ID, "dateOfBirthInput")
    month = (By.CSS_SELECTOR, '.react-datepicker__month-select')
    year = (By.CSS_SELECTOR, '.react-datepicker__year-select')
    #day = (By.CSS_SELECTOR, '.react-datepicker__day--017')
    day = lambda x: (By.XPATH, f'//div[contains(@class, "react-datepicker__day--{x:03d}") and not(@class="react-datepicker__day--outside-month")]')
    subjects = (By.ID, "subjectsInput")
    subjects_value = (By.XPATH, "//*[contains(text(), 'English')]")
    picture = (By.CSS_SELECTOR, 'input[type="file"]')
    address = (By.CSS_SELECTOR, 'textarea#currentAddress')
    state = (By.ID, "state")
    state_value = (By.XPATH, "//*[contains(text(), 'NCR')]")
    city = (By.ID, "city")
    city_value = (By.XPATH, "//*[contains(text(), 'Delhi')]")
    submit_button = (By.ID, "submit")


class AutomatonPracticeForm(BasePage):

    def set_firstname(self, firstname):
        with allure.step('first name input'):
            self.set_text(Locators.first_name, firstname)

    def set_lastname(self, lastname):
        with allure.step('last name input'):
            self.set_text(Locators.last_name, lastname)

    def set_email(self, email):
        with allure.step('email name input'):
            self.set_text(Locators.email, email)

    def set_gender(self, word):
        with allure.step('gender input'):
            if word == '1':
                self.object_click(Locators.gender_male)
            elif word == '2':
                self.object_click(Locators.gender_female)
            else:
                self.object_click(Locators.gender_other)

    def set_mobile(self, mobile):
        with allure.step('mobile input'):
            self.set_text(Locators.mobile, mobile)

    def open_calendar(self):
        with allure.step('open calendar'):
            self.object_click(Locators.date)
            #self.input_clear(Locators.date)

    def set_month(self, month):
        with allure.step('month input'):
            self.set_select(Locators.month, month)

    def set_year(self, year):
        with allure.step('year input'):
            self.set_select(Locators.year, year)

    def set_day(self, day):
        with allure.step('day input'):
            #self.set_object_click(Locators.day)
            self.object_click(Locators.day(day))

    def set_subject(self, word):
        with allure.step('subject input'):
            self.set_text(Locators.subjects, word)
            self.object_click(Locators.subjects_value)

    def set_picture(self, path):
        with allure.step('image input'):
            self.set_text(Locators.picture, path)

    def set_address(self, address):
        with allure.step('address input'):
            self.set_text(Locators.address, address)

    def set_state(self):
        with allure.step('state input'):
            self.object_click(Locators.state)
            self.object_click(Locators.state_value)

    def set_city(self):
        with allure.step('city input'):
            self.object_click(Locators.city)
            self.object_click(Locators.city_value)

    def click_submit(self):
        with allure.step('submit button click'):
            self.object_click(Locators.submit_button)

