from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class Locators:
    """
    CreateAccountPage locators
    """
    FIRST_NAME = (By.ID, "customer_firstname")



class CreateAccountPage(BasePage):
    """
    CreateAccountPage Objects
    """
    def choose_gender(self, gender):
        pass

    def enter_first_name(self, first_name):
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(first_name)


    def _verify_page(self):
        # TODO: improve this
        sleep(3)


