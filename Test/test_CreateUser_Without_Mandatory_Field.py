import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
from POM.CreateUserPage import CreateUserPage
from POM.LandingPage import LandingPage
from POM.LoginPage import LoginPage
from Utils import utils as utils
import HtmlTestRunner



@pytest.mark.usefixtures("test_setup")
class TestCreateUserWithoutMandatoryField():


    def test_CreateUserWithoutMandatoryField(self):
        driver = self.driver
        driver.get(utils.URL)
        lp = LandingPage(driver)
        lp.click_Go_Login()
        time.sleep(2)
        lop = LoginPage(driver)
        #check = lop.verify_IsChecked()
        #browser.assertTrue(check, "Está la opción Create Account tildada")
        time.sleep(2)
        lop.submit_Continue()
        time.sleep(2)
        cup = CreateUserPage(driver)
        time.sleep(2)
        cup.submit_Button_Continue_whitout_Mandatory_field()
        time.sleep(2)
        x = cup.show_error_Mandatory_Field()
        assert x == '×\nError: You must agree to the Privacy Policy!'
        print(Fore.RED +"Error not entering mandatory fields")
        assert cup.show_Mandatory_Field_First_Name() == 'First Name must be between 1 and 32 characters!'
        assert cup.show_Mandatory_Field_Last_Name() == 'Last Name must be between 1 and 32 characters!'
        assert cup.show_Mandatory_Field_Email() == 'Email Address does not appear to be valid!'
        assert cup.show_Mandatory_Field_Address() == 'Address 1 must be between 3 and 128 characters!'
        assert cup.show_Mandatory_Field_City() == 'City must be between 3 and 128 characters!'
        assert cup.show_Mandatory_Field_Region() == 'Please select a region / state!'
        assert cup.show_Mandatory_Field_Zipcode() == 'Zip/postal code must be between 3 and 10 characters!'
        assert cup.show_Mandatory_Field_LoginName() == 'Login name must be alphanumeric only and between 5 and 64 characters!'
        assert cup.show_Mandatory_Field_Password() == 'Password must be between 4 and 20 characters!'
        print(Fore.RED +"A new account could not be created, as the mandatory fields are all empty")
        print(Fore.RED +"All alert messages have been displayed, for empty mandatory fields")



    if __name__ == '__main__':
         unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)