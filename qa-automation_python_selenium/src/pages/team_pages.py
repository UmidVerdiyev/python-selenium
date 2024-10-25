import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.utils.wait_util import WaitUtil
from src.utils.js_util import JSUtil
from src.utils.logger_util import logger

class TeamPage(BasePage):
    PAGE_HEAD_SECTION = (By.ID, "page-head")
    ALL_JOBS_BUTTON = (By.XPATH, "(//a[@class='btn btn-info rounded mr-0 mr-md-4 py-3'])[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_page_loaded(self):
        logger.info("Checking if the Team Page head section is loaded.")
        return WaitUtil.wait_for_element_to_be_visible(self.driver, self.PAGE_HEAD_SECTION)

    def open_all_jobs(self, retries=3, delay=2):

        logger.info("Attempting to open 'All Jobs' section.")
        for attempt in range(1, retries + 1):
            try:
                WaitUtil.wait_for_element_to_be_visible(self.driver, self.PAGE_HEAD_SECTION)
                logger.info("Team Page head section is visible.")

                all_jobs_button = self.find_element(self.ALL_JOBS_BUTTON)
                JSUtil.scroll_into_view(self.driver, all_jobs_button)
                logger.info("Scrolled 'All Jobs' button into view.")

                JSUtil.click_element(self.driver, self.ALL_JOBS_BUTTON)
                logger.info("Clicked on 'All Jobs' button successfully.")
                break

            except (NoSuchElementException, ElementClickInterceptedException, TimeoutException) as e:
                logger.warning(f"Attempt {attempt}/{retries} failed: {e}")
                if attempt < retries:
                    logger.info(f"Retrying to click 'All Jobs' button in {delay} seconds.")
                    time.sleep(delay)
                else:
                    logger.error("Failed to click 'All Jobs' button after multiple attempts.")
                    raise e
