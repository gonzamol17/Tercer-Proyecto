import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
from POM.LandingPage import LandingPage
from POM.ProductPage import ProductPage
from POM.ForgotLoginPage import ForgotLoginPage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
from POM.ContactUsPage import ContactUsPage
import HtmlTestRunner
from Utils import utils as utils

@pytest.mark.sanity
@pytest.mark.usefixtures("test_setup")
class TestDownloadAndOpenPdf():


    def test_Verify_DownloadAndOpenPdfFile(self):
        driver = self.driver
        path = 'C:\\Users\\admin\\Downloads\\size-fit-guide-print.pdf'
        lp = LandingPage(driver)
        pp = ProductPage(driver)
        lp.select_ApparelAndT_Shirts()
        time.sleep(2)
        pp.selectTshirtTresCuarto()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(2)
        pp.selectDownloadTab()
        time.sleep(2)
        pp.selectDownloadButton()
        time.sleep(3)
        os.system(path)
        time.sleep(4)


