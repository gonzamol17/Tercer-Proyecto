import time
import pytest
import unittest
import sys
import os

from BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.LandingPage import LandingPage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
from POM.ShampooPage import ShampooPage
from Utils import utils as utils


class TestGiveReview(BaseClass):

    def test_Give_Review(self):
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
        my = MyAccountPage(driver)
        my.select_HairCare_Shampoo()
        time.sleep(2)
        sp = ShampooPage(driver)
        time.sleep(2)
        sp.viewPantene()
        time.sleep(2)
        sp.selectReview()
        driver.execute_script("window.scrollTo(0, 800)")
        time.sleep(2)
        sp.setCalification()
        time.sleep(2)
        sp.setName("Gonzalo")
        time.sleep(2)
        sp.setReview("Me gusta este perfume, pero me causó una reacción alérgica")
        time.sleep(2)
        sp.clickSubmitBtn()
        time.sleep(2)
        error = sp.errorWithoutCode()
        #assert "Human verification has failed! Please try again." in sp.errorWithoutCode()
        assert "Human verification has failed!" in sp.errorWithoutCode()
        print("Al no cargar el código requerido, se está mostrando un mensaje de error: "+sp.errorWithoutCode())

