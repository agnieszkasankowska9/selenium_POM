from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.create_account_page import CreateAccountPage
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Locators:
    CREATE_ACCOUNT_EMAIL = (By.ID, "email_create")
    CREATE_ACCOUNT_BTN = (By.ID, "SubmitCreate")

class AuthenticationPage(BasePage):
    """
    Authentication Page Object
    """
    def enter_create_account_email(self, email):
        self.driver.find_element(*Locators.CREATE_ACCOUNT_EMAIL).send_keys(email)

    def click_create_account(self):
        """
        Click create account button
        :return:
        """
        self.driver.find_element(*Locators.CREATE_ACCOUNT_BTN).click()
        return CreateAccountPage(self.driver)

    def _verify_page_title(self):
        WebDriverWait(self.driver, 10).until(EC.title_is("Login - PrestaShop"))
