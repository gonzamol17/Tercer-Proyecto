import unittest
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import time
from POM.MyAccountPage import MyAccountPage
import HtmlTestRunner
from Utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestSwitchBetweenThreeWindows():


    def test_SwitchBetweenThreeWindows(self):
        driver = self.driver
        #driver.get(utils.URL)
        time.sleep(2)
        account = MyAccountPage(driver)
        driver.execute_script("window.scrollTo(0, 4000)")
        time.sleep(2)
        print("\nEl título de la Tab principal es: "+driver.title)
        assert driver.title == "A place to practice your automation skills!"
        account.selectBtnContribute()
        account.selectLinkAbanteCard()
        #este driver.window_handles, devuelve la lista de todas las ventanas abiertas hasta el momento
        windows = driver.window_handles
        print("Los Id's de las ventanas abiertas son: "+str(windows))
        long = len(windows)
        print("La cantidad de ventanas abiertas es: "+str(long))
        aux = long-1
        n = 2
        while aux >= 1:

            driver.switch_to.window(driver.window_handles[aux])
            print("La url de la tab "+str(aux)+" es: "+driver.current_url)
            print("El título de tab "+str(aux)+" es: " + driver.title)
            assert driver.current_url == "https://www.abantecart.com/" or driver.current_url == "https://www.abantecart.com/contribute-to-abantecart"
            aux = aux-1
            time.sleep(2)
            driver.close()

        time.sleep(2)
        driver.switch_to.window(driver.window_handles[aux])
        print("Estoy de vuelta en la tab "+str(aux)+" y el título es: "+driver.title)
        print("La url de la tab "+str(aux)+" es: "+driver.current_url)
        assert driver.current_url == "https://automationteststore.com/"
        time.sleep(2)



    if __name__ == '__main__':
                unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
                    output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)
