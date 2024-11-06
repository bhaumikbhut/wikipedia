import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time

class TestAppiumSearch(unittest.TestCase):
    def setUp(self) -> None:
      
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.automation_name = 'uiautomator2'
        options.device_name = 'Pixel_9_Pro_API_30'  
        options.app_package = 'org.wikipedia.alpha'  
        options.app_activity = 'org.wikipedia.main.MainActivity' 
        options.language = 'en'
        options.locale = 'US'

     
        appium_server_url = 'http://localhost:4723'

   
        self.driver = webdriver.Remote(appium_server_url, options=options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_search_for_new_york(self) -> None:
        time.sleep(5)

        search_bar = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")
        search_bar.click()
        time.sleep(5)
        search_bar = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='org.wikipedia.alpha:id/search_src_text']")
        search_bar.send_keys("New York")
        time.sleep(2)  

        result = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='New York']")
        self.assertIsNotNone(result, "Search results for 'New York' not found!")

        close_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Clear query")  # Adjust if needed
        close_button.click()  
        time.sleep(1)
        close_button.click()  

        time.sleep(2)

        print("Test completed successfully: Search, clear, and return to home.")

if __name__ == '__main__':
    unittest.main()
