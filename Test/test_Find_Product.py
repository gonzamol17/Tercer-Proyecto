import unittest
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
import time
from POM.LandingPage import LandingPage
from POM.LoginPage import LoginPage
from POM.ProductPage import ProductPage
from POM.MyAccountPage import MyAccountPage
import HtmlTestRunner
from Utils import utils as utils


@pytest.mark.slow
@pytest.mark.usefixtures("test_setup")
class TestFindProduct():

    def test_FindProduct(self):
        driver = self.driver
        driver.get(utils.URL)
        time.sleep(2)
        # ir a login page
        lp = LandingPage(driver)
        lp.click_Go_Login()
        logpa = LoginPage(driver)
        time.sleep(2)
        # Esto permite el logueo
        logpa.do_Login("gonza_mol", "Chicharito10")
        my = MyAccountPage(driver)
        my.seleccionar_Búsqueda("Frenche")
        my.ejecutar_Búsqueda_Glass()
        #estas lineas comentadas es para ejecutar una búsqueda de un producto usando la tecla Enter
        #my = MyAccountPage(driver)
        #my.ejecutar_Búsqueda_Enter(miel)
        pp = ProductPage(driver)

        try:
            name = pp.verify_Existing_Product()
            assert "French" in name
            print("Y el titulo encontrado es " + Fore.BLUE + name)

        except:
            #print(Fore.BLUE +"No se ha encontrado un título que contenga la palabra buscada")
            #pp = ProductPage(driver)
            #print(pp.verify_Title_Of_Product_Not_Fund())
            name = pp.verify_Title_Of_Product_Not_Fund()
            assert name == 'There is no product that matches the search criteria.'
            print(Fore.BLUE + "The searched product has not been found, on the page, showing the following message \n" + name)




    if __name__ == '__main__':
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
                output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)


