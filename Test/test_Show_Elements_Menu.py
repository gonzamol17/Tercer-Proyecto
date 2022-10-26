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
class TestShowElementsMenu():


    def test_ShowElementsMenu(self):
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
        n = account.getNumberMenuItems()
        print(Fore.RED+Style.BRIGHT+"La cantidad de elementos en el menú es: "+str(n))
        time.sleep(2)
        m = account.getMenuItems()
        print(Fore.MAGENTA+"Los elementos del menú son: \n")
        time.sleep(2)
        aux = 0
        items = ['HOME', '  APPAREL & ACCESSORIES', '  MAKEUP', '  SKINCARE', '  FRAGRANCE', '  MEN', '  HAIR CARE', '  BOOKS']
        for idx, menu in enumerate(m, start=1):
            assert menu.text == items[aux]
            aux = aux+1
            print(Style.BRIGHT+Fore.MAGENTA+str(idx), menu.text)



    if __name__ == '__main__':
                unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
                    output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)