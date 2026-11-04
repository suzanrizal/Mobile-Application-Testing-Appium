from appium.webdriver.common.appiumby import AppiumBy

class Loginpage:

    def __init__(self, driver):
        self.driver = driver

        # Store Locator
        start_accessibility_ID = "Start"
        sign_up_accessibility_ID = "Sign up"
        set_name_accessibility_ID = "NAME"
        set_email_accessibility_ID = "Email"
        
