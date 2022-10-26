import unittest
import pytest
import sys
import os

from selenium.webdriver.common.by import By

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
import time
from POM.MyAccountPage import MyAccountPage
import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.usefixtures("test_setup")

class TestVerify_BannersHomePage():


    def test_Verify_BannersHomePage(self):
        driver = self.driver
        # driver.get(utils.URL)
        time.sleep(2)
        account = MyAccountPage(driver)
        print(Fore.GREEN +"\ncantidad de banners "+str(len(account.getBannersHome()))+Fore.RESET)
        tit1 = account.getTitleBanner1()
        tit2 = account.getTitleBanner2()
        tit3 = account.getTitleBanner3()
        print(Fore.GREEN+"\nTitulo del primer banner"+Fore.RESET)
        for i in tit1:
            print(i.text)
        assert "REALISTIC ONLINE STORE!" in i.text


        print("\n")
        print(Fore.GREEN +"Titulo del segundo banner"+Fore.RESET)
        for i in tit2:
           time.sleep(3)

           #list2=[]
           #list2.append(i.text)
           print(i.text)
           #assert i.text == "Learn Automation Testing\nTHE RIGHT WAY\nREALISTIC ONLINE STORE!"
        assert "THE REAL WORLD" in i.text

        print("\n")
        print(Fore.GREEN +"Titulo del tercer banner"+Fore.RESET)
        time.sleep(3)
        for i in tit3:
            print(i.text)
            #list3 = []
            #list3.append(i.text)

        assert "70% faster than manual testing" in i.text


        # print("\n")
        # print("\n")
        # aux = account.getBannersHome()
        # n = 1
        # val = []
        # for i in aux:
        #     print(i.text)
        #     aux1 = account.recorrerCiclo(n)
        #     val.append(aux1)
        #     n = n+1

    if __name__ == '__main__':
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
                output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)
