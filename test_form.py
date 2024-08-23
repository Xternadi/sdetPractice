import allure
import pytest

from automation_practice_form import AutomatonPracticeForm

firstname = "Алексей"
lastname = "Кузнецов"
email = "horizondd73@gmail.com"
gender = "2"  # 1 - male, 2 - female, другое значение - other
mobile = "1234567890"
month = "2"  # № месяца по порядку 0 - январь, 11 - декабрь
year = "1994"
day = 18
subject = "eng"  # для смены предмета, указать в этой переменной первые несколько букв
# и указать название полностью в селекторе subjects_value
image = "C:/Users/horiz/OneDrive/Desktop/sdet-main/1.png"  # перед запуском указать корректный путь
address = "Ульяновская область, город Димитровград, Алтайская ул., д. 1"

#для постпроверки
first_and_last_name_check = firstname + " " + lastname
gender_check = "Female"  # для проверки корректности введённых значений указать как текст из подсказки к перменной gender
date_check = str(day) + " March," + year  # при смене данных вместо March указать название месяца на eng
# из переменной month
subject_check = "English"  # должен = тексту из селектора subjects_value
image_check = "1.png"  # указать имя файла
Hobbies_check = ""
state_snd_city_check = "NCR" + " " + "Delhi"  # Должны совпадать с словами м в локаторе state_value и city_value


#для постпроверки


class Test:

    @pytest.mark.practiceForm
    @allure.feature('Practice form')
    @allure.story('Practice form')
    def test_practice_form(self, browser):
        form_page = AutomatonPracticeForm(browser)
        with allure.step('open page'):
            form_page.open_site()
        with allure.step('input first name'):
            form_page.set_firstname(firstname)
        with allure.step('input last name '):
            form_page.set_lastname(lastname)
        with allure.step('email name input'):
            form_page.set_email(email)
        with allure.step('set gender'):
            form_page.set_gender(gender)
        with allure.step('mobile input'):
            form_page.set_mobile(mobile)
        with allure.step('set date'):
            form_page.open_calendar()
            form_page.set_month(month)
            form_page.set_year(year)
            form_page.set_day(day)
        with allure.step('subject input'):
            form_page.set_subject(subject)
        with allure.step('choose image'):
            form_page.choose_image(image)
        with allure.step('address input'):
            form_page.set_address(address)
        with allure.step('state and city input'):
            form_page.set_state()  # Для изменения: заменить слово в локаторе state_value
            # в файле automation_practice_form
            form_page.set_city()  # Для изменения: заменить слово в локаторе state_city
            # в файле automation_practice_form
        with allure.step('click submit'):
            form_page.click_submit()
        with allure.step('post condition and data verification'):
            form_page.check_title(browser)
            assert form_page.check_result(first_and_last_name_check, email, gender_check, mobile, date_check,
                                          subject_check, Hobbies_check, image_check, address, state_snd_city_check) == True
        with allure.step('browser close'):
            browser.quit()

# pytest -s -v --alluredir results
# allure serve results