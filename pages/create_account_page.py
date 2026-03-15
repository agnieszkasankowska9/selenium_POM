from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from utils.custom_types import Gender
from selenium.webdriver.support.select import Select


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



class CreateAccountPage(BasePage):
    """
    CreateAccountPage Objects
    """
    def select_gender(self, gender):
        """
        Choose Mr. or Mrs.
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
        # TODO: improve this

        sleep(3)

    def select_date_of_birth(self, date_of_birth):
        """
        selectin date of birth
        :return:
        """
        birth_day = Select(self.driver.find_element(*Locators.BIRTH_DAY_SELECT))
        birth_day.select_by_value(str(date_of_birth.day))

