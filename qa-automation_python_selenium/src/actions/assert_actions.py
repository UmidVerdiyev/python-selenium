import logging

class AssertActions:
    def __init__(self, logger):
        self.logger = logger

    def assert_text(self, actual, expected, message=""):
        self.logger.info(f"Asserting text: Expected: '{expected}', Actual: '{actual}'")
        assert actual == expected, message

    def assert_element_present(self, element, message=""):
        self.logger.info(f"Asserting element presence: {element}")
        assert element is not None, message
