from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, timeout=10):

        self.driver = driver
        self.timeout = timeout

    def find_element(self, locator):

        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} was not found after {self.timeout} seconds")

    def find_elements(self, locator):

        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Elements with locator {locator} were not found after {self.timeout} seconds")

    def click(self, locator):

        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):

        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):

        element = self.find_element(locator)
        return element.text

    def is_element_visible(self, locator):

        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False

    def get_title(self):

        return self.driver.title



    def wait_for_url(self, url):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.url_contains(url))
        except TimeoutException:
            return False
