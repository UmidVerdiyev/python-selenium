from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))

    def take_screenshot(self, file_name):
        self.driver.save_screenshot(file_name)
