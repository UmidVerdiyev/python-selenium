from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class DriverFactory:
    @staticmethod
    def get_driver(driver_type):
        driver_type = driver_type.lower()
        if driver_type == 'chrome':
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=ChromeOptions())
        elif driver_type == 'firefox':
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=FirefoxOptions())
        else:
            raise Exception('Unknown driver type: {}'.format(driver_type))
