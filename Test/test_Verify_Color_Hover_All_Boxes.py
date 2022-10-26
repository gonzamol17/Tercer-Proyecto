import unittest
import pytest
import sys
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
import time
from POM.LandingPage import LandingPage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
import HtmlTestRunner
from Utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestVerifyColorHoverAllBoxes():


    def test_Verify_Color_Hover_All_Boxes(self):
        driver = self.driver
        time.sleep(2)
        lp = LandingPage(driver)
        lp.click_Go_Login()
        logpa = LoginPage(driver)
        time.sleep(2)
        logpa.do_Login("gonza_mol", "Chicharito10")
        account = MyAccountPage(driver)
        numbox = len(account.getAllBoxes())
        box = account.getAllBoxes()
        print(Fore.GREEN +"\nLa cantidad de boxes en My Account es: "+str(numbox)+Fore.RESET)
        n = 1
        # solución2
        # for i in box:
        #    boxn= driver.find_element(By.CSS_SELECTOR,"div.col-md-9.col-xs-12.mt20>div>ul>li:nth-child(" + str(n) + ")>a")
        #    hover = ActionChains(driver).move_to_element(driver.find_element(By.CSS_SELECTOR,"div.col-md-9.col-xs-12.mt20>div>ul>li:nth-child(" + str(n) + ")>a"))
        #    hover.perform()
        #    assert 'rgba(242, 92, 39, 1)' in boxn.value_of_css_property('background-color')
        #    n = n+1
        #
        # print(Fore.GREEN + "\nAl hacer hover sobre cada icono en My Account, se está visualizando el color esperado " + Fore.RESET)
        # print(Fore.YELLOW + boxn.value_of_css_property('background-color') + " Que representa naranja" + Fore.RESET)

        #solución1
        for i in box:
            aux = account.getIndividualBox(n)
            assert 'rgba(245, 245, 245, 1)' in aux.value_of_css_property('background-color')
            hover = ActionChains(driver).move_to_element(aux)
            hover.perform()
            assert 'rgba(242, 92, 39, 1)' in aux.value_of_css_property('background-color')
            n = n+1

        print(Fore.GREEN +"\nAl hacer hover sobre cada icono en My Account, se está visualizando el color esperado "+Fore.RESET)
        print(Fore.YELLOW+aux.value_of_css_property('background-color')+" Que representa naranja"+Fore.RESET)
