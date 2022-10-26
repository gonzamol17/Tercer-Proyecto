import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
from POM.LandingPage import LandingPage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
from POM.ContactUsPage import ContactUsPage
import HtmlTestRunner
from Utils import utils as utils

@pytest.mark.sanity
@pytest.mark.usefixtures("test_setup")
class TestVerifyMandatoryFieldContactUs():


    def test_Verify_Mandatory_Fields_ContactUs(self):
        driver = self.driver
        #driver.get(utils.URL)
        time.sleep(2)
        # ir a login page
        lp = LandingPage(driver)
        lp.click_Go_Login()
        logpa = LoginPage(driver)
        time.sleep(2)
        # Esto permite el logueo
        logpa.do_Login("gonza_mol", "Chicharito10")

        account = MyAccountPage(driver)
        account.seleccionar_ContactUs_Option()
        time.sleep(2)
        cu = ContactUsPage(driver)
        print(cu.verificar_ContactUs_Form())
        time.sleep(2)
        assert cu.verificar_ContactUs_Form() == "Contact Us Form"
        print(Fore.GREEN + "Estoy en la página de Contact Us")
        time.sleep(2)
        cu.sendForm()
        time.sleep(3)
        name = cu.get_FirstName()
        email = cu.get_Email()
        enquiry = cu.get_Enquiry()
        assert name == "First name: is required field! Name must be between 3 and 32 characters!"
        assert email == "Email: is required field! E-Mail Address does not appear to be valid!"
        assert enquiry == "Enquiry: is required field! Enquiry must be between 10 and 3000 characters!"

        print("Todos los mensajes de validación de campos mandatorios se están mostrando")
        print(Fore.RED +"\n"+name)
        print(Fore.RED +"\n"+email)
        print(Fore.RED +"\n"+enquiry)



        if __name__ == '__main__':
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
                output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)




