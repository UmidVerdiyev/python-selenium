from src.pages.home_page import HomePage
from src.pages.careers_page import CareersPage
from src.pages.open_postions_page import OpenPositionsPage
from src.pages.team_pages import TeamPage


class PageManager:
    def __init__(self, driver):
        self.driver = driver

    def home_page(self):
        return HomePage(self.driver)

    def careers_page(self):
        return CareersPage(self.driver)

    def open_positions_page(self):
        return OpenPositionsPage(self.driver)
    def team_page(self):
        return TeamPage(self.driver)
