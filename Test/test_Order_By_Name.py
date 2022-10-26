import unittest
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
import time
from POM.MyAccountPage import MyAccountPage
import HtmlTestRunner
from Utils.screenShotNoUSAR import Screen



@pytest.mark.usefixtures("test_setup")

class TestVerify_Testimonials():


    def test_Order_By_Name(self):
        driver = self.driver
        #driver.get(utils.URL)
        time.sleep(2)
        account = MyAccountPage(driver)
        account.seleccionar_Producto_Books_Paperback()
        ss = Screen(driver)
        time.sleep(2)
        account.selectOrderByNameA_Z("Name A - Z")
        time.sleep(2)
        lista1 = ["ALLEGIANT BY VERONICA ROTH", "PAPER TOWNS BY JOHN GREEN","THE MIRACLE MORNING: THE NOT-SO-OBVIOUS SECRET GUARANTEED TO TRANSFORM YOUR LIFE"]
        paper = account.getListOfPaperback()
        name = account.getNameOfPaperback()
        print(Fore.MAGENTA+"\nEl número de paperback en la página es: "+str(len(account.getListOfPaperback()))+Fore.RESET)
        lista2 = []
        n = 0
        b = 0
        for i in name:
            lista2.append(i.text)
            #print(Fore.CYAN+i.text+Fore.RESET)
            if lista2[n] == lista1[n]:
                assert lista2[n] == lista1[n]
                print(Fore.CYAN + i.text + Fore.RESET)
                n = n+1
            else:
                print(Fore.RED+"Los elementos no están ordenados alfabéticamente"+Fore.RESET)
                b = 1
                break
        if b == 1:
            print(Fore.RED+"No se muestra nada ya que no están ordenados alfabéticamente"+Fore.RESET)
        else:
            print(Fore.GREEN+"Todos los productos están ordenados alfabéticamente (A-Z)"+Fore.RESET)
            print(Fore.GREEN+"El orden de los paperback listados es: " + str(lista2)+Fore.RESET)



if __name__ == '__main__':
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
                output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)
