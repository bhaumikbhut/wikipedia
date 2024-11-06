import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time

class TestAppiumSearch(unittest.TestCase):
    def setUp(self) -> None:
        # Set up Appium capabilities
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.automation_name = 'uiautomator2'
        options.device_name = 'Pixel_9_Pro_API_30'  # Replace with your device/emulator name
        options.app_package = 'org.wikipedia.alpha'  # App package for Wikipedia
        options.app_activity = 'org.wikipedia.main.MainActivity'  # Replace with the correct activity
        options.language = 'en'
        options.locale = 'US'

        # URL of Appium server
        appium_server_url = 'http://localhost:4723'

        # Initialize the driver
        self.driver = webdriver.Remote(appium_server_url, options=options)

    def tearDown(self) -> None:
        # Clean up by quitting the driver
        if self.driver:
            self.driver.quit()

    def test_search_for_new_york(self) -> None:
        # Step 1: Wait for the app to load
        time.sleep(5)

        # Step 2: Locate the search bar and click on it
        search_bar = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")
        search_bar.click()
        time.sleep(5)
        search_bar = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='org.wikipedia.alpha:id/search_src_text']")
        # Step 3: Type "New York" into the search bar
        search_bar.send_keys("New York")
        time.sleep(2)  # Wait for the results to appear

        # Step 4: Assert that the search results are displayed (e.g., by checking for "New York" in the result list)
        result = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='New York']")
        self.assertIsNotNone(result, "Search results for 'New York' not found!")

        # Step 5: Find the close button and double-click it to clear the search bar
        close_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Clear query")  # Adjust if needed
        close_button.click()  # Click once
        time.sleep(1)
        close_button.click()  # Click again to return to home

        # Step 6: Wait for the app to return to the home page 
        time.sleep(2)

        print("Test completed successfully: Search, clear, and return to home.")

if __name__ == '__main__':
    unittest.main()
