from appium import webdriver
from appium.options.android import UiAutomator2Options

class DriverSetup:
    def __init__(self):
        self.driver = None

    def start_driver(self):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = "RZ8M31KMW6Z"  # Replace with your actual device name
        options.app_package = "com.mumzworld.android"
        options.app_activity = "com.mumzworld.android.MainActivity"
        options.no_reset = True
        options.new_command_timeout = 1000  # seconds

        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        return self.driver

    def stop_driver(self):
        if self.driver:
            self.driver.quit()
