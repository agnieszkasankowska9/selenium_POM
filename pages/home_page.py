from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.authentication_page import AuthenticationPage

class Locators:
    """
    Home Page elements Locators
    """
    SIGN_IN_LINK = (By.CLASS_NAME, "login")

class HomePage(BasePage):
    """
    Home Page Object
    """
    def click_sign_in(self):
        """
        Click sign in and goes to Authentication Page
        :return: AuthenticationPage object
        """
        self.driver.find_element(*Locators.SIGN_IN_LINK).click()
        return AuthenticationPage(self.driver)
