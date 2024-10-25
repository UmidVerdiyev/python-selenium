from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class WaitUtil:
    timeout = 60

    @staticmethod
    def wait_for_element_to_be_clickable(driver, locator, timeout=10):
        try:
            WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise TimeoutException(f"Element {locator} is not clickable after {timeout} seconds")

    @staticmethod
    def wait_for_element_to_be_visible(driver, locator, timeout=30):
        try:
            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Element {locator} is not visible after {timeout} seconds")

    @staticmethod
    def wait_for_element_locate(driver, locator, timeout=60):
        try:
            return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Element {locator} was not located after {timeout} seconds")

    @staticmethod
    def wait_for_new_window(driver, number_of_windows, timeout=10):
        try:
            WebDriverWait(driver, timeout).until(lambda d: len(d.window_handles) == number_of_windows)
        except TimeoutException:
            raise TimeoutException(f"Expected {number_of_windows} windows, but did not get them after {timeout} seconds")
    @staticmethod
    def wait_for_url_to_contain(driver, text, timeout=10):
        try:
            WebDriverWait(driver, timeout).until(EC.url_contains(text))
        except TimeoutException:
            raise TimeoutException(f"URL did not contain '{text}' after {timeout} seconds")