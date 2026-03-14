from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Locators:
    CREATE_ACCOUNT_EMAIL = (By.ID, "email_create")

class AuthenticationPage(BasePage):
    """
    Authentication Page Object
    """
    def enter_create_account_email(self, email):
        self.driver.find_element(*Locators.CREATE_ACCOUNT_EMAIL).send_keys(email)
