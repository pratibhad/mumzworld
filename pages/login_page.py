from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").text("Email")'
        ).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").text("Password")'
        ).send_keys(password)

    def click_login(self):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("auth-primary-action")'
        ).click()

    def is_logged_in(self):
        return self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("Sign Out"))'
        ).is_displayed()
