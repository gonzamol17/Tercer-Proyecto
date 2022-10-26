import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.CreateUserPage import CreateUserPage
from POM.LandingPage import LandingPage
from POM.LoginPage import LoginPage
import HtmlTestRunner
from Utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestUserAlreadyBeenCreated():


    def test_UserAlreadyBeenCreated(self):
        driver = self.driver
        #driver.get(utils.URL)
        lp = LandingPage(driver)
        lp.click_Go_Login()
        time.sleep(2)
        lop = LoginPage(driver)
        #check = lop.verify_IsChecked()
        #browser.assertTrue(check, "Está la opción Create Account tildada")
        time.sleep(2)
        lop.submit_Continue()
        time.sleep(2)
        account = CreateUserPage(driver)
        time.sleep(2)
        account.complete_All_Field_For_New_Account("Gonzalo", "Molina", "gonzalo.molina@darwoft.com",
                                                   "Sol de Mayo 550", "Cordoba", "5000", "gonza_mol", "Chicharito10",
                                                   "Chicharito10")

        time.sleep(2)
        account.create_Country("Argentina")
        time.sleep(2)
        account.create_Region("Cordoba")
        time.sleep(2)
        account.submit_Button_Continue_whitout_Mandatory_field()
        time.sleep(2)
        x = account.show_Existing_User_Message()
        print(x)
        assert x == '×\nError: E-Mail Address is already registered!'
        print("The user could not be created, because it already exists in the system")




    if __name__ == '__main__':
         unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)