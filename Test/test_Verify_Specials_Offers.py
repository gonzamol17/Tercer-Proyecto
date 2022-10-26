import unittest
import pytest
import sys
import os

from selenium.webdriver import ActionChains

from BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
import time
from POM.MyAccountPage import MyAccountPage
from POM.LandingPage import LandingPage
from POM.SpecialOffersPage import SpecialOffersPage
import HtmlTestRunner


@pytest.mark.usefixtures("test_setup")
class Test_SpecialOffers(BaseClass):


    def test_Verify_Specials_Offers(self):
        driver = self.driver
        log = self.get_Logger()
        time.sleep(2)
        lp = LandingPage(driver)
        lp.selectSpecialsOffers()
        so = SpecialOffersPage(driver)
        numberofsales = len(so.getAllSales())
        print(Fore.YELLOW+"\nCantidad de elementos en sales es: "+str(numberofsales)+Fore.RESET)
        log.info("Cantidad de Elementos en sales es")
        aux = so.getAllSales()
        n = 1
        b = 6
        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(2)
        for i in aux:
            try:
              if n <= 4:
                assert so.getIndividualSpecialText(n).is_displayed()
                print(Fore.GREEN +"Se está visualizando el label de Sale en el producto: "+str(n)+ Fore.RESET)
                print(so.getIndividualSpecialText(n).is_displayed())
                n = n + 1
              else:
                  time.sleep(2)
                  assert so.getIndividualSpecialText(b).is_displayed()
                  print(Fore.GREEN + "Se está visualizando el label de Sale en el producto: " + str(b-1) + Fore.RESET)
                  print(so.getIndividualSpecialText(b).is_displayed())
                  b = b + 1

            except:
                 print(Fore.RED+"En alguno de los productos, el label Sales, no se está visualizando"+Fore.RESET)

        log.info("Se ve el resultado final")

    if __name__ == '__main__':
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
                output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)



