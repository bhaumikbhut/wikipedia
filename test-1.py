import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        # Define the capabilities using UiAutomator2Options
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.automation_name = 'uiautomator2'
        options.device_name = 'Pixel 9 Pro API 30'
        options.app_package = 'org.wikipedia.alpha'
        options.app_activity = 'org.wikipedia.main.MainActivity'  # Launch main activity, not settings
        options.language = 'en'
        options.locale = 'US'

        # Set the Appium server URL
        self.appium_server_url = 'http://localhost:4723'

        # Initialize the driver with options
        self.driver = webdriver.Remote(self.appium_server_url, options=options)

    def tearDown(self) -> None:
        # Close the session
        if self.driver:
            self.driver.quit()

    def test_scroll_and_click_icons(self) -> None:
        # Wait for the app to fully load
        time.sleep(5)

        # Step 1: Scroll down to the end
        self.scroll_down()

        # Step 2: Click on "My lists" icon
        self.click_and_wait("My lists")

        # Step 3: Click on "History" icon
        self.click_and_wait("History")

        # Step 4: Click on "Nearby" icon
        self.click_and_wait("Nearby")

        # Step 5: Go back to home by clicking the "Browse" icon
        self.click_browse_icon()

        # Step 6: Scroll up to the first topic
        self.scroll_up()

    def scroll_down(self):
        """Scroll down to the bottom of the page."""
        screen_height = self.driver.get_window_size()['height']
        screen_width = self.driver.get_window_size()['width']
        
        # Coordinates for swipe: swipe down from (middle, bottom) to (middle, top)
        start_x = screen_width // 2
        start_y = screen_height * 3 // 4
        end_y = screen_height // 4
        
        self.driver.swipe(start_x, start_y, start_x, end_y, 800)
        time.sleep(2)  # Wait for scrolling to finish

    def scroll_up(self):
        """Scroll up to the top of the page."""
        screen_height = self.driver.get_window_size()['height']
        screen_width = self.driver.get_window_size()['width']
        
        # Coordinates for swipe: swipe up from (middle, top) to (middle, bottom)
        start_x = screen_width // 2
        start_y = screen_height // 4
        end_y = screen_height * 3 // 4
        
        self.driver.swipe(start_x, start_y, start_x, end_y, 800)
        time.sleep(2)  # Wait for scrolling to finish

    def click_and_wait(self, icon_name: str):
        """Click on an icon and wait for 3 seconds."""
        try:
            icon = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=icon_name)
            icon.click()
            time.sleep(3)
        except Exception as e:
            print(f"Failed to click on {icon_name}: {e}")

    def click_browse_icon(self):
        """Click on the 'Browse' icon to return to home."""
        try:
            browse_icon = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Explore")
            browse_icon.click()
            time.sleep(2)
        except Exception as e:
            print(f"Failed to click on Browse icon: {e}")

if __name__ == '__main__':
    unittest.main()
