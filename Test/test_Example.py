import sys
import os
from BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import time
from Utils import utils as utils


class TestGiveReview(BaseClass):

    def test_setUpClass(self):
        driver = self.driver
        driver.get(utils.URL)
        time.sleep(2)
        title = driver.title
        print(title)
        currenturl = driver.current_url
        print(currenturl)
        driver.get("https://courses.letskodeit.com/login")
        currenturl = driver.current_url
        print(currenturl)
        time.sleep(2)
        driver.back()
        currenturl = driver.current_url
        print(currenturl)
        time.sleep(2)
        driver.forward()
        currenturl = driver.current_url
        print(currenturl)
