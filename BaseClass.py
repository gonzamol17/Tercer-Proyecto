import inspect
import logging
import pytest


@pytest.mark.usefixtures("test_setup")
class BaseClass:

    def get_Logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("..\\Datos\\logfile.log")
        #fileHandler = logging.FileHandler("C:\\Users\\User\\PycharmProjects\\Tercer-Proyecto\\Datos\\logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

