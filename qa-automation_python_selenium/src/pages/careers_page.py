from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.utils.js_util import JSUtil
from src.utils.wait_util import WaitUtil


class CareersPage(BasePage):

    CAREERS_URL = "https://useinsider.com/careers/"


    PAGE_HEAD_SECTION = (By.ID, "page-head")
    READY_TO_DISRUPT_TITLE = (By.XPATH, "//h1[contains(text(), 'Ready to disrupt?')]")
    FIND_YOUR_CALLING_SECTION = (By.ID, "career-find-our-calling")
    FIND_YOUR_CALLING_TITLE = (By.XPATH, "//h3[contains(text(), 'Find your calling')]")
    OUR_LOCATION_SECTION = (By.ID, "career-our-location")
    OUR_LOCATIONS_TITLE = (By.XPATH, "//h3[contains(text(), 'Our Locations')]")
    LIFE_AT_INSIDER_TITLE = (By.XPATH, "//h2[contains(text(), 'Life at Insider')]")
    SEE_ALL_TEAMS = (By.LINK_TEXT, "See all teams")

    def __init__(self, driver):
        super().__init__(driver)

    def is_life_at_insider_section_opened(self):

        return self.is_element_visible(self.LIFE_AT_INSIDER_TITLE)

    def is_locations_section_opened(self):

        return self.is_element_visible(self.OUR_LOCATION_SECTION) and self.is_element_visible(self.OUR_LOCATIONS_TITLE)

    def is_teams_section_opened(self):

        return self.is_element_visible(self.FIND_YOUR_CALLING_SECTION) and self.is_element_visible(self.FIND_YOUR_CALLING_TITLE)

    def is_page_loaded(self):

        return self.is_element_visible(self.PAGE_HEAD_SECTION) and self.is_element_visible(self.READY_TO_DISRUPT_TITLE)

    def click_see_all_teams(self):

        WaitUtil.wait_for_element_to_be_clickable(self.driver, self.SEE_ALL_TEAMS)
        JSUtil.scroll_into_view(self.driver, self.find_element(self.FIND_YOUR_CALLING_TITLE))
        JSUtil.click_element(self.driver, self.SEE_ALL_TEAMS)

    def select_team(self, title):

        team_name_locator = (By.XPATH, f"//h3[contains(text(), '{title}')]")
        WaitUtil.wait_for_element_to_be_visible(self.driver, team_name_locator)
        JSUtil.scroll_into_view(self.driver, self.find_element(team_name_locator))
        JSUtil.click_element(self.driver, team_name_locator)

    def navigate_to_specific_team_page(self, team_name):

        self.click_see_all_teams()
        self.select_team(team_name)
