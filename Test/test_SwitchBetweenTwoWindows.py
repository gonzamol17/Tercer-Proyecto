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
class TestSwitchBetweenTwoWindows():


    def test_SwitchBetweenTwoWindows(self):
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
        time.sleep(2)
        account = MyAccountPage(driver)
        account.selectLinkFb()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        print(Fore.GREEN+"+++++++++++++++++DATOS PESTAÑA Facebook+++++++++++++++++++++++++++++++++++"+Fore.RESET)
        time.sleep(2)
        aux1 = driver.current_window_handle
        aux2 = aux1.replace('CDwindow-',' ')
        print("El número de ventana 2 es: "+aux2)
        time.sleep(2)
        print("La url de la ventana 2 es: "+driver.current_url)
        print("El nombre de la Tab de la ventana 2 es: "+driver.title)
        assert driver.title == "Facebook - Inicia sesión o regístrate"
        print(Fore.GREEN + "++++++++++++++++++++++++++++++DATOS PESTAÑA Automation Test Store++++++++++++++++++++" + Fore.RESET)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        aux3 = driver.current_window_handle
        aux4 = aux3.replace('CDwindow-', ' ')
        print("El número de ventana 1 es: " + aux4)
        print("La url de la ventana 1 es: "+driver.current_url)
        print("El nombre de la Tab de la ventana 1 es: " + driver.title)
        assert driver.title == "My Account"





    if __name__ == '__main__':
                unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
                    output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)