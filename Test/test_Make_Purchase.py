import time
import pytest
import unittest
import sys
import os

from POM.CheckoutConfirmationPage import CheckoutConfirmationPage
from POM.CheckoutStatus import CheckoutStatus
from POM.ProductPage import ProductPage

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
from POM.LandingPage import LandingPage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
from POM.LipsPage import LipsPage
from POM.ShoppingCartPage import ShoppingCartPage
import HtmlTestRunner

@pytest.mark.usefixtures("test_setup")
class TestMakePurchase():


    def test_MakePurchase(self):
        driver = self.driver
        #driver.get(utils.URL)
        time.sleep(2)
        #ir a login page
        lp = LandingPage(driver)
        lp.click_Go_Login()
        logpa = LoginPage(driver)
        time.sleep(2)
        #Esto permite el logueo
        logpa.do_Login("gonza_mol", "Chicharito10")
        time.sleep(2)
        #Verifico que no tenga nada en el carrito de Compras
        scp = ShoppingCartPage(driver)
        my = MyAccountPage(driver)
        my.seleccionar_Cart_Option()

        try:
            assert scp.check_Label_Without_Element() == 'Your shopping cart is empty!\nContinue'
            my.seleccionar_Producto_Makeup()
        except:
            #scp.clean_Shopping_Cart()
            print(Fore.RED + "La cantidad de Productos a eliminar del carrito es: " + str(scp.contar_Elementos_Eliminados()))
            scp.clean_List_Of_Products()
            time.sleep(2)
            scp.click_Btn_Continue()
            time.sleep(2)
            my.seleccionar_Producto_Makeup()
        # Acá selecciono La pagina del producto(lapiz labial) para agregarlo a carrito e ir a la pagina de producto
        scp = ShoppingCartPage(driver)
        time.sleep(2)
        lip = LipsPage(driver)
        lip.add_Cart1()
        time.sleep(2)
        # Acá creo un objeto del  tipo de producto elegido, y selecciono el color, y la cantidad y verifico que coincido lo que pido
        pp = ProductPage(driver)
        pp.select_Product_Lips_Color_And_Qty("Viva Glam II", "3")
        time.sleep(2)
        #Aca estando en ShoppingCartPage verifico que el color sea el elegido, el precio unitario, la cantidad, y el precio total
        assert scp.show_Color() == 'Color Viva Glam II'
        print("\n")
        print(Fore.BLUE + "Acá empiezan todas las validaciones en la Página Shopping Cart:")
        print(Fore.BLUE + "==============================================================\n")
        print(Fore.GREEN + "El color elegido es: " + scp.show_Color())
        time.sleep(2)
        assert scp.show_Unit_Price() == '$5.00'
        print(Fore.GREEN + "El precio unitario del producto es: " + scp.show_Unit_Price())
        time.sleep(2)
        assert scp.show_Quantity() == '3'
        print(Fore.GREEN + "La cantidad del producto elegido es: " + scp.show_Quantity())
        time.sleep(2)
        assert scp.show_Total_Amount() == '$15.00'
        print(Fore.GREEN + "El precio total de los productos elegidos es: " + scp.show_Total_Amount())
        time.sleep(2)
        scp.do_Checkout()
        time.sleep(2)
        # Acá creo un objeto del tipo checkoutconfirmationpage, y antes de confirmar el pedido valido algunos labels
        ccp = CheckoutConfirmationPage(driver)
        # acá van todas las validaciones de label y titulos
        print("\n")
        print(Fore.LIGHTYELLOW_EX + "--------------------------------------------------------------------\n")
        print(Fore.BLUE + "Acá empiezan todas las validaciones en la página Checkout Confirmation:")
        print(Fore.BLUE + "======================================================================\n")
        assert ccp.show_Title() == "CHECKOUT CONFIRMATION"
        print(Fore.CYAN + "Se encuentra el título: " + ccp.show_Title())
        assert ccp.show_Subtitle() == "Shipping"
        print(Fore.CYAN + "Se encuentra el subtitulo: " + ccp.show_Subtitle())
        assert ccp.show_Name_Shipping() == "Gonzalo Molina\n223232323"
        print(Fore.CYAN + "Está el nombre del usuario buscado: " + ccp.show_Name_Shipping())
        assert ccp.show_Address_Shipping() == "Sol de Mayo 550 Mandioca 2400, 2do Piso\nCórdoba Cordoba 5000\nArgentina"
        print(Fore.CYAN + "Está el domicilio del usuario: " + ccp.show_Address_Shipping())
        assert ccp.show_Flat_Shipping() == "Flat Shipping Rate"
        print(Fore.CYAN + "Está el título " + ccp.show_Flat_Shipping())
        assert ccp.show_Order_Summary() == "ORDER SUMMARY"
        print(Fore.CYAN + "Está el titulo " + ccp.show_Order_Summary())
        assert ccp.show_Qty_Color() == "3 x Viva Glam Lipstick\n- Color Viva Glam II"
        print(Fore.CYAN + "Está el color y la cantidad solicitada: " + ccp.show_Qty_Color())
        assert ccp.show_Unit_Price() == "$5.00"
        print(Fore.CYAN + "El precio unitario es " + ccp.show_Unit_Price())
        assert ccp.show_Sub_Total() == "$15.00"
        print(Fore.CYAN + "El subtotal es: " + ccp.show_Sub_Total())
        assert ccp.show_Flat_Shipping_Rate() == "$2.00"
        print(Fore.CYAN + "El costo de envío fijo es " + ccp.show_Flat_Shipping_Rate())
        assert ccp.show_Total() == "$17.00"
        print(Fore.CYAN + "El costo total es: " + ccp.show_Total())
        assert ccp.show_Payment_Title() == "Payment"
        print(Fore.CYAN + "Está la sección " + ccp.show_Payment_Title())
        assert ccp.show_Name_Payment() == "Gonzalo Molina\n223232323"
        print(Fore.CYAN + "El nombre del usuario está " + ccp.show_Name_Payment())
        assert ccp.show_Address_Payment() == "Sol de Mayo 550 Mandioca 2400, 2do Piso\nCórdoba Cordoba 5000\nArgentina"
        print(Fore.CYAN + "Está la dirección del usuario " + ccp.show_Address_Payment())
        assert ccp.show_Cash_Deliveryt() == "Cash On Delivery"
        print(Fore.CYAN + "Está el título " + ccp.show_Cash_Deliveryt())
        # con este botón ya confirmo el pedido
        ccp.do_Checkout_Confirmation()
        time.sleep(2)
        # Acá ya obtengo la confirmación exitosa del pedido
        cs = CheckoutStatus(driver)
        time.sleep(2)
        assert cs.get_Message_Alternative() == 'You can view your order details by going to the invoice page.'
        time.sleep(2)
        print("\n")
        print(Fore.GREEN + "La orden ha sido procesada exitosamente")
        time.sleep(2)
        cs.select_Button_Continue()
        time.sleep(2)
        # Acá verifico que una vez comprado el producto, vuelva a la Landing Page (homepage)
        lp = LandingPage(driver)
        assert lp.verificar_Nombre_Landing_Page() == 'Welcome back Gonzalo'
        print("\n")
        print(Fore.GREEN + "Estas en la página Home")
        time.sleep(2)




    if __name__ == '__main__':
         unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)