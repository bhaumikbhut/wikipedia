import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time

class TestAppiumSettings(unittest.TestCase):

    def setUp(self) -> None:
        # Define Appium capabilities
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.automation_name = 'uiautomator2'
        options.device_name = 'Pixel_9_Pro_API_30'  # Replace with your device/emulator name
        options.app_package = 'org.wikipedia.alpha'  # Package name of Wikipedia
        options.app_activity = 'org.wikipedia.main.MainActivity'  # Main activity of Wikipedia
        options.language = 'en'
        options.locale = 'US'

        # Appium server URL
        appium_server_url = 'http://localhost:4723'

        # Initialize the driver
        self.driver = webdriver.Remote(appium_server_url, options=options)

    def tearDown(self) -> None:
        # Clean up by quitting the driver
        if self.driver:
            self.driver.quit()

    def test_disable_all_options_in_settings(self) -> None:
        # Step 1: Wait for the app to load
        time.sleep(5)

        # Step 2: Click on the settings icon
        settings_icon = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@content-desc='More options']")  
        settings_icon.click()
        time.sleep(2)
        settings =  self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@resource-id='org.wikipedia.alpha:id/explore_overflow_settings']")
        settings.click()
        # Step 3: Wait for the settings screen to appear
        time.sleep(2)

        # Step 4: Disable all options 
    
        show_images_toggle = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.Switch[@resource-id='org.wikipedia.alpha:id/switchWidget'])[1]")
      
        show_images_toggle.click() 

        time.sleep(2)

        show_link_previews_toggle = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.Switch[@resource-id='org.wikipedia.alpha:id/switchWidget'])[2]")
     
        show_link_previews_toggle.click()  

        time.sleep(2)
        

        send_usage_reports = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.Switch[@resource-id='org.wikipedia.alpha:id/switchWidget'])[3]")

        send_usage_reports.click()  

        time.sleep(2)
        
        send_crash_reports = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.Switch[@resource-id='org.wikipedia.alpha:id/switchWidget'])[4]")
       
        send_crash_reports.click() 

        time.sleep(2) 

        # Step 5: Go back to the home page 
        back_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Navigate up") 
        back_button.click()

        # Step 6: Wait for the home page to load
        time.sleep(2)

        print("Settings updated and returned to the home page successfully.")

if __name__ == '__main__':
    unittest.main()
