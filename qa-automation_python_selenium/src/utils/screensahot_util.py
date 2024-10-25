import os
from datetime import datetime

class ScreenshotUtil:
    @staticmethod
    def take_screenshot(driver, name="screenshot"):
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
