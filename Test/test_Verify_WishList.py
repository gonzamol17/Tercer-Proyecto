import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
from POM.MyAccountPage import MyAccountPage
from POM.LandingPage import LandingPage
from POM.LoginPage import LoginPage
from POM.ShoppingCartPage import ShoppingCartPage
from POM.LipsPage import LipsPage
from POM.ProductPage import ProductPage
from POM.WishListPage import WishListPage
import HtmlTestRunner



@pytest.mark.usefixtures("test_setup")
class TestVerifyWishList():


    def test_VerifyWishList(self):
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
        scp = ShoppingCartPage(driver)
        my = MyAccountPage(driver)
        my.select_HairCare_Shampoo()
        time.sleep(2)
        lip = LipsPage(driver)
        time.sleep(4)
        lip.select_LipsProduct()
        time.sleep(2)
        # Acá creo un objeto del  tipo de producto elegido, y selecciono el color, y la cantidad y verifico que coincido lo que pido
        pp = ProductPage(driver)
        time.sleep(3)
        try:
            pp.Add_Wish_List()

        except:
            pp.Remove_Wish_List()
            pp.Add_Wish_List()

        time.sleep(3)
        product = pp.verify_Existing_Product()
        lp = LandingPage(driver)
        lp.Select_My_Wish_List_Option()
        wl = WishListPage(driver)
        assert product == wl.verify_product_added()
        print(Fore.GREEN + "El producto seleccionado " + product + " coincide con el de Mi lista de deseos  " + wl.verify_product_added())


        if __name__ == '__main__':
                unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
                    output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)
