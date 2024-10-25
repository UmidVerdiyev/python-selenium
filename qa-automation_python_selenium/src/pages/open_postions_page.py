import time
from selenium.common.exceptions import (
    NoSuchElementException, StaleElementReferenceException, TimeoutException, ElementClickInterceptedException
)
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.utils.js_util import JSUtil
from src.utils.wait_util import WaitUtil
from src.utils.logger_util import logger


class OpenPositionsPage(BasePage):
    FILTER_BY_LOCATION_CONTAINER = (By.XPATH, "//span[@id='select2-filter-by-location-container']")
    FILTER_BY_DEPARTMENT_CONTAINER = (By.XPATH, "//span[@id='select2-filter-by-department-container']")
    JOBS_LIST = (By.XPATH, "//*[@id='jobs-list']")
    VIEW_ROLE_BUTTON = (By.XPATH, ".//a[contains(text(), 'View Role')]")
    ACCEPT_COOKIES_BUTTON = (By.LINK_TEXT, "Accept All")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def accept_cookies(self):
        logger.info("Attempting to accept cookies.")
        try:
            WaitUtil.wait_for_element_to_be_clickable(self.driver, self.ACCEPT_COOKIES_BUTTON, timeout=10)
            self.find_element(self.ACCEPT_COOKIES_BUTTON).click()
            logger.info("Cookies accepted.")
        except TimeoutException:
            logger.warning("No cookies acceptance button found.")

    def select_location(self, location, retries=3, delay=5):
        logger.info(f"Selecting location: {location}")
        for attempt in range(1, retries + 1):
            try:
                # Wait for and click the location filter dropdown
                WaitUtil.wait_for_element_to_be_clickable(self.driver, self.FILTER_BY_LOCATION_CONTAINER)
                location_dropdown = self.find_element(self.FILTER_BY_LOCATION_CONTAINER)
                JSUtil.scroll_into_view(self.driver, location_dropdown)
                location_dropdown.click()

                location_option = (By.XPATH,
                                   f"//li[contains(@id, 'select2-filter-by-location-result') and contains(text(), '{location}')]")
                self.find_element(location_option).click()
                logger.info(f"Location '{location}' selected successfully.")

                WaitUtil.wait_for_element_to_be_visible(self.driver, self.JOBS_LIST, timeout=30)
                break

            except (NoSuchElementException, TimeoutException, ElementClickInterceptedException) as e:
                logger.warning(f"Attempt {attempt}/{retries} failed to select location: {e}")
                if attempt < retries:
                    logger.info(f"Retrying to select location in {delay} seconds.")
                    time.sleep(delay)
                else:
                    logger.error(f"Failed to select location '{location}' after multiple attempts.")
                    raise

    def select_department(self, department, retries=3, delay=5):

        logger.info(f"Selecting department: {department}")
        for attempt in range(1, retries + 1):
            try:
                WaitUtil.wait_for_element_to_be_clickable(self.driver, self.FILTER_BY_DEPARTMENT_CONTAINER)
                department_dropdown = self.find_element(self.FILTER_BY_DEPARTMENT_CONTAINER)
                JSUtil.scroll_into_view(self.driver, department_dropdown)
                department_dropdown.click()

                department_option = (By.XPATH,
                                     f"//li[contains(@id, 'select2-filter-by-department-result') and contains(text(), '{department}')]")
                self.find_element(department_option).click()
                logger.info(f"Department '{department}' selected successfully.")

                WaitUtil.wait_for_element_to_be_visible(self.driver, self.JOBS_LIST, timeout=30)
                break

            except (NoSuchElementException, TimeoutException, ElementClickInterceptedException) as e:
                logger.warning(f"Attempt {attempt}/{retries} failed to select department: {e}")
                if attempt < retries:
                    logger.info(f"Retrying to select department in {delay} seconds.")
                    time.sleep(delay)
                else:
                    logger.error(f"Failed to select department '{department}' after multiple attempts.")
                    raise

    def click_view_role(self, retries=3, delay=5):

        logger.info("Attempting to click on 'View Role' button.")
        for attempt in range(1, retries + 1):
            try:
                self.accept_cookies()

                job_title_locator = (
                By.XPATH, "//p[contains(@class, 'position-title') and contains(text(), 'Quality Assurance')]")
                job_location_locator = (
                By.XPATH, "//div[contains(@class, 'position-location') and contains(text(), 'Istanbul, Turkey')]")
                view_role_button_locator = self.VIEW_ROLE_BUTTON

                WaitUtil.wait_for_element_to_be_visible(self.driver, job_title_locator)
                WaitUtil.wait_for_element_to_be_visible(self.driver, job_location_locator)

                view_role_button = self.find_element(view_role_button_locator)
                JSUtil.scroll_into_view(self.driver, view_role_button)
                JSUtil.click_element(self.driver, view_role_button_locator)
                logger.info("Clicked 'View Role' button successfully.")

                WaitUtil.wait_for_new_window(self.driver, 2)
                new_window = \
                [window for window in self.driver.window_handles if window != self.driver.current_window_handle][0]
                self.driver.switch_to.window(new_window)
                logger.info("Switched to Lever Application form tab.")
                break

            except (StaleElementReferenceException, TimeoutException, NoSuchElementException,
                    ElementClickInterceptedException) as e:
                logger.warning(f"Attempt {attempt}/{retries} to click 'View Role' failed: {e}")
                if attempt < retries:
                    logger.info(f"Retrying to click 'View Role' button in {delay} seconds.")
                    time.sleep(delay)
                else:
                    logger.error("Failed to click 'View Role' button after multiple attempts.")
                    self.driver.refresh()
                    self.accept_cookies()
                    time.sleep(delay)
                    raise
