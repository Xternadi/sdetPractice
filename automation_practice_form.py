from selenium.webdriver.common.by import By

from base_page import BasePage


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
    day = lambda x: (By.XPATH,
                     f'//div[contains(@class, "react-datepicker__day--{x:03d}")\
                      and not(@class="react-datepicker__day'f'--outside-month")]')
    subjects = (By.ID, "subjectsInput")
    subjects_value = (By.XPATH, "//*[contains(text(), 'English')]")
    picture = (By.CSS_SELECTOR, 'input[type="file"]')
    address = (By.CSS_SELECTOR, 'textarea#currentAddress')
    state = (By.ID, "state")
    state_value = (By.XPATH, "//*[contains(text(), 'NCR')]")
    city = (By.ID, "city")
    city_value = (By.XPATH, "//*[contains(text(), 'Delhi')]")
    submit_button = (By.ID, "submit")
    table_string1 = (By.XPATH, "//*/table/tbody/tr[1]/td[2]")
    table_string2 = (By.XPATH, "//*/table/tbody/tr[2]/td[2]")
    table_string3 = (By.XPATH, "//*/table/tbody/tr[3]/td[2]")
    table_string4 = (By.XPATH, "//*/table/tbody/tr[4]/td[2]")
    table_string5 = (By.XPATH, "//*/table/tbody/tr[5]/td[2]")
    table_string6 = (By.XPATH, "//*/table/tbody/tr[6]/td[2]")
    table_string7 = (By.XPATH, "//*/table/tbody/tr[7]/td[2]")
    table_string8 = (By.XPATH, "//*/table/tbody/tr[8]/td[2]")
    table_string9 = (By.XPATH, "//*/table/tbody/tr[9]/td[2]")
    table_string10 = (By.XPATH, "//*/table/tbody/tr[10]/td[2]")


class AutomatonPracticeForm(BasePage):

    def set_firstname(self, firstname):
        self.set_text(Locators.first_name, firstname)

    def set_lastname(self, lastname):
        self.set_text(Locators.last_name, lastname)

    def set_email(self, email):
        self.set_text(Locators.email, email)

    def set_gender(self, word):
        if word == '1':
            self.object_click(Locators.gender_male)
        elif word == '2':
            self.object_click(Locators.gender_female)
        else:
            self.object_click(Locators.gender_other)

    def set_mobile(self, mobile):
        self.set_text(Locators.mobile, mobile)

    def open_calendar(self):
        self.object_click(Locators.date)

    def set_month(self, month):
        self.set_value_for_select(Locators.month, month)

    def set_year(self, year):
        self.set_value_for_select(Locators.year, year)

    def set_day(self, day):
        self.object_click(Locators.day(day))

    def set_subject(self, word):
        self.set_text(Locators.subjects, word)
        self.object_click(Locators.subjects_value)

    def choose_image(self, path):
        self.set_text(Locators.picture, path)

    def set_address(self, address):
        self.set_text(Locators.address, address)

    def set_state(self):
        self.object_click(Locators.state)
        self.object_click(Locators.state_value)

    def set_city(self):
        self.object_click(Locators.city)
        self.object_click(Locators.city_value)

    def click_submit(self):
        self.object_click(Locators.submit_button)

    def check_title(self, browser):
        element = browser.find_element(By.ID, "example-modal-sizes-title-lg")
        if not element:
            return False
        else:
            return True

    def check_result(self, first_and_last_name_check, email, gender_check, phone, date_check, subject_check,
                     Hobbies_check, image_check, address, state_snd_city_check):
        if (
                self.verification(Locators.table_string1, first_and_last_name_check) == True and
                self.verification(Locators.table_string2, email) == True and
                self.verification(Locators.table_string3, gender_check) == True and
                self.verification(Locators.table_string4, phone) == True and
                self.verification(Locators.table_string5, date_check) == True and
                self.verification(Locators.table_string6, subject_check) == True and
                self.verification(Locators.table_string7, Hobbies_check) == True and
                self.verification(Locators.table_string8, image_check) == True and
                self.verification(Locators.table_string9, address) == True and
                self.verification(Locators.table_string10, state_snd_city_check) == True
        ):
            return True
        else:
            return False
