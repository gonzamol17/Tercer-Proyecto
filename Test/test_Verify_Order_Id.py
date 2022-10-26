import re
import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
from POM.LandingPage import LandingPage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
from POM.LipsPage import LipsPage
from POM.ProductPage import ProductPage
from POM.ShoppingCartPage import ShoppingCartPage
from POM.CheckoutConfirmationPage import CheckoutConfirmationPage
from POM.My_Order_History import My_Order_History
import HtmlTestRunner
from Utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestVerifyOrder():


    def test_VerifyOrder(self):
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
        # Acá selecciono La pagina del producto(lapiz labial) para agregarlo a carrito e ir a la pagina de producto
        scp = ShoppingCartPage(driver)
        my = MyAccountPage(driver)
        my.seleccionar_Producto_Makeup()
        time.sleep(2)
        lip = LipsPage(driver)
        lip.add_Cart1()
        time.sleep(2)
        # Acá creo un objeto del  tipo de producto elegido, y selecciono el color, y la cantidad y verifico que coincido lo que pido
        pp = ProductPage(driver)
        pp.select_Product_Lips_Color_And_Qty("Viva Glam II", "1")
        time.sleep(2)
        scp.do_Checkout()
        time.sleep(2)
        time.sleep(2)
        # Acá creo un objeto del tipo checkoutconfirmationpage
        ccp = CheckoutConfirmationPage(driver)
        # con este botón ya confirmo el pedido
        ccp.do_Checkout_Confirmation()
        time.sleep(2)
        Order_id = ccp.show_Order_Id()
        #aux = Order_id[11:16]
        #print(aux)
        Order_number = re.findall("[0-9]", Order_id)
        Only_order_id = ''.join(Order_number)
        print(Only_order_id)

        #Acá voy a ir a Order history y busco mi order_id recientemente creado
        ccp.Select_Order_History_Option()
        moh = My_Order_History(driver)
        #print(moh.Verify_Order_History())
        #aux1 = moh.Verify_Order_History()[10:15]
        aux1 = moh.Verify_Order_History()
        assert Only_order_id in aux1
        print(Fore.GREEN+ "El id de la orden recientemente obtenida, coincide con el id último de mi historial, y es: "+moh.Verify_Order_History())



    if __name__ == '__main__':
         unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)


