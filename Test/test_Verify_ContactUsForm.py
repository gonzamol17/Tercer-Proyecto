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
class TestVerifyContactUsForm():


    def test_Verify_ContactUsForm(self):
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
        cu.fill_FirstName("gonza")
        time.sleep(2)
        cu.fill_Email("gonzalo.molina@darwoft.com")
        time.sleep(2)
        cu.fill_Enquiry("Por favor me pueden regalar un millón de pesos?")
        time.sleep(2)
        cu.sendForm()

        message = cu.Verify_Enquiry_Success()
        assert message == "Your enquiry has been successfully sent to the store owner!"



        if __name__ == '__main__':
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
                output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)



