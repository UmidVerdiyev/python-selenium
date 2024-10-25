
import pytest
from src.driver.driver_factory import DriverFactory
from src.pages.home_page import HomePage
from src.pages.careers_page import CareersPage
from src.pages.open_postions_page import OpenPositionsPage
from src.pages.team_pages import TeamPage
from src.constant.url import INSIDER_HOME
from src.utils.logger_util import logger
from src.utils.screensahot_util import ScreenshotUtil
from src.utils.wait_util import WaitUtil

@pytest.mark.usefixtures("setup")
class TestCareerPage:
    @pytest.fixture(params=["firefox" , "chrome"])
    def setup(self, request):
        self.driver = DriverFactory.get_driver(driver_type=request.param)
        self.driver.maximize_window()
        request.cls.driver = self.driver
        yield
        self.driver.quit()

    def test_career_page(self):
        try:
            logger.info("Starting test: test_career_page")

            homepage = HomePage(self.driver)
            self.driver.get(INSIDER_HOME)
            logger.info("Navigated to Insider Home Page.")

            assert homepage.is_homepage_opened(), "Homepage did not open as expected."
            logger.info("Verified Insider Home Page is opened.")

            homepage.navigate_to_careers()
            logger.info("Navigated to Careers page.")

            careers_page = CareersPage(self.driver)
            assert careers_page.is_page_loaded(), "Careers Page did not load properly."
            logger.info("Verified Careers Page is loaded.")

            careers_page.click_see_all_teams()
            logger.info("Clicked 'See All Teams' on Careers page.")

            team_page = TeamPage(self.driver)
            team_page.open_all_jobs()
            logger.info("Opened all jobs in Team page.")

            open_positions_page = OpenPositionsPage(self.driver)

            open_positions_page.select_location("Istanbul, Turkey")
            logger.info("Filtered jobs by location: Istanbul, Turkey.")

            open_positions_page.select_department("Quality Assurance")
            logger.info("Filtered jobs by department: Quality Assurance.")

            open_positions_page.click_view_role()
            logger.info("Clicked 'View Role' for Quality Assurance position in Istanbul.")

            WaitUtil.wait_for_new_window(self.driver, 2,
                                         timeout=15)
            self.driver.switch_to.window(self.driver.window_handles[-1])

            expected_url_part = "jobs.lever.co/useinsider"
            WaitUtil.wait_for_url_to_contain(self.driver, expected_url_part, timeout=10)
            assert expected_url_part in self.driver.current_url, "Did not redirect to the Lever Application form page."
            logger.info("Verified redirection to Lever Application form page.")

        except AssertionError as e:
            logger.error(f"Assertion failed: {e}")
            ScreenshotUtil.take_screenshot(self.driver, "test_career_page_failure")
            raise

        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            ScreenshotUtil.take_screenshot(self.driver, "test_career_page_unexpected_error")
            raise

        finally:
            logger.info("Test 'test_career_page' completed.")
