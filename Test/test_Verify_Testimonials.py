import unittest
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
import time
from POM.MyAccountPage import MyAccountPage
import HtmlTestRunner


@pytest.mark.usefixtures("test_setup")
class TestVerify_Testimonials():


    def test_Verify_Testimonials(self):
        driver = self.driver
        #driver.get(utils.URL)
        time.sleep(2)
        account = MyAccountPage(driver)
        driver.execute_script("window.scrollTo(0, 4000)")
        t = account.getTestimonials()
        # print("Cantidad de elementos: "+str(len(t)))
        lista1 = ['Sub_cero', '1er', '2do', '3er', '4to', '5to']
        n = 0
        for test in t:
            if n == 0 or n == 5:
                n = n + 1
            else:
                assert test.text in "Regular customer and products" or "Returns were easy and my" or "I found this store to be very reasonably" or "Really great products"
                print(Fore.GREEN + "El título del " + lista1[n] + " Testimonials es: " + Fore.RESET + test.text)
                # time.sleep(7)
                n = n + 1
                time.sleep(7)





    if __name__ == '__main__':
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
                output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)
