import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style

from POM.LandingPage import LandingPage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
import HtmlTestRunner
from Utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_Login(self):
        driver = self.driver
        #driver.get(utils.URL)
        lp = LandingPage(driver)
        lp.click_Go_Login()
        logpa = LoginPage(driver)
        time.sleep(2)
        my = MyAccountPage(driver)
        file = open("C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Datos\\Login.json", "r")
        jsondata = file.read()
        obj = json.loads(jsondata)
        list = obj['users']
        #print(list)
        #print(len(list))
        for i in range(len(list)):
            username = list[i].get("user")
            password = list[i].get("password")
            logpa.do_Login(username, password)
            print(Fore.BLUE + "Account of " + username)
            account = MyAccountPage(driver)
            try:
                x = account.verificar_Ingreso_Correcto2()
                assert x == 'MY ACCOUNT'
                print(Fore.GREEN + "Se pudo ingresar correctamente a esta cuenta")
                time.sleep(4)
                my.seleccionar_Logoff()
                time.sleep(2)
                lp.click_Go_Login()
                time.sleep(2)
            except:
                x = logpa.show_error_username_password()
                assert x == '×\nError: Incorrect login or password provided.'
                print(Fore.RED + "No se Pudo ingresar correctamente a esta cuenta por tener incorrecta username o password")
                time.sleep(4)
                #my.seleccionar_Logoff()
                #time.sleep(2)
                lp.click_Go_Login()
                time.sleep(2)

    if __name__ == '__main__':
         unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)