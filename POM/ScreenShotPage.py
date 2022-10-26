import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By




class ScreenShotPageLocators():
    list_color = (By.CSS_SELECTOR, "#option305")


class ScreenShotPage():

    def __init__(self, driver):
        self.driver = driver

    def take_ScreenShots(self):

        try:
            fileName = str(round(time.time() * 1000)) + ".png"
            screenshotDirectory = "C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Screenshots\\"
            destinationFile = screenshotDirectory + fileName
            self.driver.save_screenshot(destinationFile)
            print("Screenshot shot saved to directory:-->" + destinationFile)
        except NoSuchElementException:
            print("Se produjo algún tipo de errror en la ejecución")