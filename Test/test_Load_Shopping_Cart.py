import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.LandingPage import LandingPage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
from POM.SkinCarePage import SkinCarePage
import HtmlTestRunner
from Utils import utils as utils



@pytest.mark.usefixtures("test_setup")
class TestLoadShoppingCart():


    def test_LoadShoppingCart(self):
        driver = self.driver
        driver.get(utils.URL)
        lp = LandingPage(driver)
        skp = SkinCarePage(driver)
        lp.click_Go_Login()
        logpa = LoginPage(driver)
        logpa.do_Login("gonza_mol", "Chicharito10")
        my = MyAccountPage(driver)
        time.sleep(2)
        my.seleccionar_Producto_SkinCare()
        time.sleep(4)
        driver.execute_script("window.scrollTo(0, 800)")
        time.sleep(4)
        skp.add_Product_Antiage()
        time.sleep(2)
        skp.add_Product_Cremenuit()
        time.sleep(2)
        skp.add_Product_Facialcream()
        time.sleep(2)
        skp.add_Product_Absolueyes()
        time.sleep(2)
        my.seleccionar_Logoff()
        print("No se confirma la compra de ninguno de los productos")
        print("Se agregaron productos al carrito de compras del usuario gonza_mol")



    if __name__ == '__main__':
         unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)