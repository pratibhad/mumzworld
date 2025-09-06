from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    def click_account_tab(self):
        account_tab = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Account")')
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(account_tab)
        ).click()

    def click_sign_in_button(self):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("Sign In")').click()

    def click_sign_out_button(self):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("Sign Out"))'
        ).click()
