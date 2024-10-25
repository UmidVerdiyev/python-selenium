from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class HomePage(BasePage):
    COMPANY_MENU = (By.LINK_TEXT, "Company")
    CAREERS_LINK = (By.LINK_TEXT, "Careers")

    def is_homepage_opened(self):

        return "Insider" in self.get_title()

    def navigate_to_careers(self):

        self.click(self.COMPANY_MENU)
        self.click(self.CAREERS_LINK)
