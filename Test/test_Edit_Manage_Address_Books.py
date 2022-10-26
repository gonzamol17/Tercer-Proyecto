import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
import time
from POM.LandingPage import LandingPage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
from Utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class Test_Edit_Manage_Address_Books():


    def test_Edit_Manage_Address_Books(self):
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
        account = MyAccountPage(driver)
        n = account.getQuantityOfAddressBook()
        assert n != 0
        print(Fore.MAGENTA+"Se tiene al menos una dirección ingresada y es: "+Fore.RESET+Fore.GREEN+n+Fore.RESET)
        time.sleep(2)
        account.selectBoxManageAddressBook()
        time.sleep(2)
        account.selectBtnEditAddressBook()
        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(2)
        account.setAddressTwoAddressBook("Mandioca 2400, 2do Piso")
        time.sleep(3)
        account.saveBtnAddressBook()
        time.sleep(3)
        message = account.getAlertMessageAddressBook()
        assert message in "×\nYour address has been successfully updated"
        assert 'rgba(60, 118, 61, 1)' in account.getObjectAlertMessageAddressBook().value_of_css_property('color')
        time.sleep(3)
        print(Fore.MAGENTA+"Se muestra el mensaje y color correcto de dirección editada "+Fore.GREEN+message[2:44]+Fore.RESET)
        time.sleep(2)
        print(Fore.MAGENTA+"Toda la información editada que se tiene de Address Book Entries es: \n"+account.getAllAddressBook())
        assert "Mandioca 2400, 2do Piso" in account.getAllAddressBook()
        print("La nueva segunda dirección editada/agregada, está dentro de Address Book Entries correctamente")
        time.sleep(2)





