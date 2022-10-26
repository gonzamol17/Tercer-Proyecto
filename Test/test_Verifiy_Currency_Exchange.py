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
from POM.ShoppingCartPage import ShoppingCartPage
from POM.ShampooPage import ShampooPage
import HtmlTestRunner


@pytest.mark.sanity
@pytest.mark.usefixtures("test_setup")
class TestVerifyCurrencyExchange():

    def test_Verify_ContactUsForm(self):
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

        # Verifico que no tenga nada en el carrito de Compras
        scp = ShoppingCartPage(driver)
        my = MyAccountPage(driver)
        my.seleccionar_Cart_Option()

        try:
            assert scp.check_Label_Without_Element() == 'Your shopping cart is empty!\nContinue'
            lp.Select_Euro_Currency()
            my.select_HairCare_Shampoo()
        except:
            # scp.clean_Shopping_Cart()
            print(Fore.RED + "La cantidad de Productos eliminados del carrito fueron: " + str(
                scp.contar_Elementos_Eliminados()))
            scp.clean_List_Of_Products()
            time.sleep(2)
            scp.click_Btn_Continue()
            time.sleep(2)
            lp.Select_Euro_Currency()
            my.select_HairCare_Shampoo()
        time.sleep(4)
        # selecciono la moneda Euro
        #lp.Select_Euro_Currency()
        sp = ShampooPage(driver)
        time.sleep(4)
        sp.add_Fragance()
        currencyfrangance = sp.get_PriceFragance()
        titlefragance = sp.get_TitleFragance()
        time.sleep(4)
        sp.add_Pantene()
        currencypantene = sp.get_PricePantene()
        titlepantene = sp.get_TitlePantene()
        driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(4)

        my.open_ItemBox()
        time.sleep(4)
        productfragance = my.get_TitleFragance()
        productshampoo = my.get_TitleShampoo()

        assert titlefragance == productfragance
        assert titlepantene == productshampoo
        assert "€" in currencypantene
        assert "€" in currencyfrangance
        print(Fore.GREEN +"Se encontraron dos productos en el box de Items")
        print(Fore.GREEN + "Los dos productos encontrados en el box de Item, son los que se seleccionaron anteriormente")
        print(Fore.GREEN + "y ambos precios están en moneda Euro")





        if __name__ == '__main__':
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
                output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)


