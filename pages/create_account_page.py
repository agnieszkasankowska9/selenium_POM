from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from utils.custom_types import Gender
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Locators:
    """
    CreateAccountPage locators
    """
    FIRST_NAME = (By.ID, "customer_firstname")
    GENDER_MALE = (By.XPATH, '//label[@for="id_gender1"]')
    GENDER_FEMALE = (By.XPATH, '//label[@for="id_gender2"]')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    BIRTH_DAY_SELECT = (By.ID, "days")
    BIRTH_MONTH_SELECT = (By.ID, "months")
    BIRTH_YEAR_SELECT = (By.ID, "years")
    REGISTER_BTN = (By.ID, "submitAccount")
    VISIBLE_ERRORS = (By.XPATH, '//div[@class="alert alert-danger"]/ol/li')
    NUMBER_VISIBLE_ERRORS = (By.XPATH, '//div[@class="alert alert-danger"]/p')


class CreateAccountPage(BasePage):
    """
    CreateAccountPage Objects
    """
    def choose_gender(self, gender):
        """
        Choose Mr or Mrs
        """
        if gender == Gender.MALE:
            self.driver.find_element(*Locators.GENDER_MALE).click()
        else:
            self.driver.find_element(*Locators.GENDER_FEMALE).click()


    def enter_first_name(self, first_name):
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(first_name)


    def get_entered_email(self):
        """
        email entered on previous page
        :return:
        """
        return self.driver.find_element(*Locators.EMAIL).get_attribute("value")

    def enter_password(self, password):
        """
        type password
        """
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)

    def _verify_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.FIRST_NAME))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.REGISTER_BTN))



    def select_date_of_birth(self, date_of_birth):
        """
        selectin date of birth
        :return:
        """
        birth_day = Select(self.driver.find_element(*Locators.BIRTH_DAY_SELECT))
        birth_day.select_by_value(str(date_of_birth.day))
        birth_month = Select(self.driver.find_element(*Locators.BIRTH_MONTH_SELECT))
        birth_month.select_by_value(str(date_of_birth.month))
        birth_year = Select(self.driver.find_element(*Locators.BIRTH_YEAR_SELECT))
        birth_year.select_by_value(str(date_of_birth.year))

    def get_visible_errors(self):
        """
        Return all visible errors
        """
        errors_webelements = self.driver.find_element(*Locators.VISIBLE_ERRORS)
        visible_errors = []
        for error in errors_webelements:
            visible_errors.append(error.text)
        return visible_errors

    def get_number_of_errors_message(self):
        return self.driver.find_element(*Locators.NUMBER_VISIBLE_ERRORS).text

    def click_register_button (self):
        self.driver.find_element(*Locators.REGISTER_BTN).click()



