import time


class Screen:

    def __init__(self, driver):
        self.driver = driver

    # este método es usado en el test que se llama test_Order_By_Name
    def screenshot(self):
        try:
            screenshotDirectory = "C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Screenshots\\"
            fileName = time.asctime().replace(":","_") + ".png"
            destinationFile = screenshotDirectory + fileName
            self.driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory:-->" + destinationFile)

        except:
            print("Por alguna razón no se pudo capturar la imagen donde está fallando el Test Case")
