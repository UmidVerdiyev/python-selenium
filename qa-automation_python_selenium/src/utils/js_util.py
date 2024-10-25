class JSUtil:

    @staticmethod
    def scroll_into_view(driver, element):
        driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @staticmethod
    def click_element(driver, locator):

        element = driver.find_element(*locator)
        driver.execute_script("arguments[0].click();", element)

    @classmethod
    def scroll_down(cls, driver):
        pass
