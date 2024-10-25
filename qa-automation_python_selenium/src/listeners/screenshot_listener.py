import pytest
from src.utils.screensahot_util import ScreenshotUtil

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    driver = item.funcargs.get("driver")

    if rep.when == 'call':
        if rep.failed:
            ScreenshotUtil.take_screenshot(driver, item.name)
            print(f"Test {item.name} failed, screenshot captured.")
        elif rep.skipped:
            print(f"Test {item.name} was skipped.")
        else:
            print(f"Test {item.name} passed successfully.")
