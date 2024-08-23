from selenium import webdriver
from selenium.webdriver.support.select import Select


class BasePage:

    def __init__(self, driver: webdriver, url="https://demoqa.com/automation-practice-form"):
        self.driver = driver
        self.base_url = url

    def open_site(self):
        return self.driver.get(self.base_url)

    def set_text(self, locator, word):
        field = self.driver.find_element(*locator)
        field.clear()
        field.send_keys(word)

    def set_value_for_select(self, locator, value):
        select_object = self.driver.find_element(*locator)
        select = Select(select_object)
        select.select_by_value(value)

    def object_click(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def verification(self, locator, value):
        element = self.driver.find_element(*locator)
        if element.text == value:
            return True
        else:
            return False


