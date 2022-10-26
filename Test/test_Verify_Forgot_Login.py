import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
from POM.LandingPage import LandingPage
from POM.ForgotLoginPage import ForgotLoginPage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
from POM.ContactUsPage import ContactUsPage
import HtmlTestRunner
from Utils import utils as utils

@pytest.mark.sanity
@pytest.mark.usefixtures("test_setup")
class TestVerifyForgotLogin():


    def test_Verify_Forgot_Login_Successfully(self):
        driver = self.driver
        lp = LandingPage(driver)
        lp.click_Go_Login()
        flp = ForgotLoginPage(driver)
        lp.selectForgotLogin()
        flp.set_LastName("Molina")
        flp.set_Email("gonzalo.molina@darwoft.com")
        flp.selectBtnContinue()
        assert "Success: Your login name reminder has been sent to your e-mail address." in flp.getTextSuccesfullMessageAlert()
        print(Fore.GREEN + "Se está visualizando el mensaje de Alerta exitoso" + Fore.RESET)
        assert "rgba(223, 240, 216, 1)" == flp.getAlertSuccessMessage().value_of_css_property('background-color')
        print(Fore.GREEN+"El color de la alerta es el verde esperado"+Fore.RESET)
        flp.selecteIconCloseAlert()
        try:
            if flp.getAlertSuccessMessage().is_displayed():
                print("Se sigue verificando el alerta exitoso, y no debería aparecer")
        except:

            print(Fore.GREEN+"Ya no se está visualizando el alerta exitoso, de acuerdo a lo esperado, porque fue cerrado"+Fore.RESET)



    def test_Verify_Forgot_Login_Failed(self):
        driver = self.driver
        lp = LandingPage(driver)
        lp.click_Go_Login()
        flp = ForgotLoginPage(driver)
        lp.selectForgotLogin()
        flp.set_LastName("Lopez")
        flp.set_Email("gonzalo.molina@darwoft.com")
        flp.selectBtnContinue()
        assert "Error: No records found matching information your provided" in flp.getTextFailedMessageAlert()
        print(Fore.RED + "Se está visualizando el mensaje de Alerta fallido" + Fore.RESET)
        assert "rgba(242, 222, 222, 1)" == flp.getAlertFailedMessage().value_of_css_property('background-color')
        print(Fore.RED+"El color de la alerta es el rojo esperado"+Fore.RESET)
        flp.selecteIconCloseAlertFailed()
        try:
            if flp.getAlertFailedMessage().is_displayed():
                print("Se sigue verificando el alerta fallido, y no debería aparecer")
        except:

            print(Fore.RED+"Ya no se está visualizando el alerta exitoso, de acuerdo a lo esperado, porque fue cerrado"+Fore.RESET)