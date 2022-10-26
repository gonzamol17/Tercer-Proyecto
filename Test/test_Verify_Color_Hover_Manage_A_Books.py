import unittest
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
import time
from POM.LandingPage import LandingPage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
import HtmlTestRunner
from Utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestVerifyColorHoverManageBooks():


    def test_Verify_Color_Hover_Manage_A_Books(self):
        driver = self.driver
        time.sleep(2)
        lp = LandingPage(driver)
        lp.click_Go_Login()
        logpa = LoginPage(driver)
        time.sleep(2)
        logpa.do_Login("gonza_mol", "Chicharito10")
        account = MyAccountPage(driver)
        assert 'rgba(245, 245, 245, 1)' in account.getBoxManageBooks().value_of_css_property('background-color')
        account.select_Hover_ManageAddressBooks()
        assert 'rgba(242, 92, 39, 1)' in account.getBoxManageBooks().value_of_css_property('background-color')
        print(Fore.GREEN +"\nAl hacer hover sobre el componente de Manage Address Books, se está visualizando el color esperado "+Fore.RESET)
        print(Fore.YELLOW+account.getBoxManageBooks().value_of_css_property('background-color')+" Que es naranja"+Fore.RESET)

