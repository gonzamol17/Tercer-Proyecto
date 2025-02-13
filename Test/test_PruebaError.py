import unittest
import pytest
import sys
import os

from BaseClass import BaseClass
from collections import Counter
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
import time
from POM.MyAccountPage import MyAccountPage
from Utils.screenShotNoUSAR import Screen


class TestPruebaerror(BaseClass):


    def test_PruebaError(self):
        log = self.get_Logger()
        driver = self.driver
        #driver.get(utils.URL)
        time.sleep(2)
        account = MyAccountPage(driver)
        account.seleccionar_Producto_Books_Paperback()
        ss = Screen(driver)
        time.sleep(2)
        #account.selectOrderByNameA_Z("Name A - Z")
        name = account.getNameOfPaperback()
        lista2 = []
        n = 0
        b = 0
        for i in name:
            lista2.append(i.text)
            #print(Fore.CYAN + i.text + Fore.RESET)
        print("El orden de los paperback listados es: " + str(lista2))
        nueva_lista_actual = lista2.copy()
        print("Esta es la copia "+str(nueva_lista_actual))
        lista2.sort()
        print(lista2)
        #assert nueva_lista_actual == lista2
        #value = Counter(nueva_lista_actual) == Counter(lista2)
        aux = account.getPrueba(nueva_lista_actual, lista2)
        print(aux)
        time.sleep(2)
