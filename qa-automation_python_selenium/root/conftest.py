import pytest
from src.utils.screensahot_util import ScreenshotUtil

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshot_path = f"screenshots/{item.nodeid.replace('::', '_')}_failure.png"
            ScreenshotUtil.take_screenshot(driver, screenshot_path)

@pytest.fixture(scope="session", autouse=True)
def setup_reports():
    import os
    if not os.path.exists("reports"):
        os.makedirs("reports")
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
