from tests.base_test import BaseTest
from time import sleep
from test_data.registration_data_generator import RegistrationDataGenerator

class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.data = RegistrationDataGenerator()  #zrobi to raz
        self.authentication_page = self.home_page.click_sign_in()
        self.authentication_page.enter_create_account_email(self.data.EMAIL)
        self.create_account_page = self.authentication_page.click_create_account()


    def testNoLastName(self):
        self.create_account_page.choose_gender(self.data.GENDER)
        self.create_account_page.enter_first_name(self.data.FIRST_NAME)
        sleep(3)

