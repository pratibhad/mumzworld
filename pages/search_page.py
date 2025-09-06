import time

from appium.webdriver.common.appiumby import AppiumBy

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def explore(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().text("Explore")').click()

    def search_item(self, item_name):
        search_box =  self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").text("Search Mumzworld")'
        )
        search_box.click()
        time.sleep(2)
        search_box.send_keys(item_name)
        self.driver.execute_script('mobile: performEditorAction', {'action': 'search'})