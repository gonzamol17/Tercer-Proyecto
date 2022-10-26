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
class TestShowFooterElements():



    def test_ShowFooterElements(self):
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
        driver.execute_script("window.scrollTo(0, 700)")
        account = MyAccountPage(driver)
        n = account.contar_Footer_Component()
        print(Fore.BLUE+"la cantidad de elementos en el footer es: "+str(n))
        print(Fore.BLUE+"Los elementos del footer son:")
        m = account.mostrar_Footer_Component()
        aux = 1
        for idx, ele_foo in enumerate(m):
            if aux == 1:
                print(idx, ele_foo.text[0:9])
                aux=2
            else:
                print(idx, ele_foo.text[0:10])

    if __name__ == '__main__':
                unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
                    output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)