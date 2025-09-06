from appium.webdriver.common.appiumby import AppiumBy

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def select_first_product(self):
        self.driver.find_elements(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.view.ViewGroup")'
        )[0].click()

    def add_to_cart(self):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.TextView").text("Add to Cart")'
        ).click()

    def go_to_cart(self):
        try:
            element=self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.TextView").text("Item added to cart")'
                )
            return element.is_displayed()
        except Exception as e:
            print(f"Error in adding to cart:{e}")
            return False

    def close_cart(self):
        element =  self.driver.find_element(
        AppiumBy.XPATH,
            '//com.horcrux.svg.SvgView[@resource-id="phosphor-react-native-x-regular"]/..'
        )
        element.click()
