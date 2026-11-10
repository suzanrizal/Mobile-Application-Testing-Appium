# Import the required classes from Appium
from appium import webdriver
# Import UiAutomator2Options to configure our Android device
from appium.options.android import UiAutomator2Options
# Import Appium's locator strategies
from appium.webdriver.common.appiumby import AppiumBy
# Import time to add a small waiting period
import time
options = UiAutomator2Options()

# Specify the mobile platform
options.platform_name = "Android"
# Specify the device name
options.device_name = "Pixel 5"
# Specify the automation engine
options.automation_name = "UiAutomator2"
# Specify the Android emulator ID
options.udid = "emulator-5554"
# Specify the Calculator app package
options.app_package = "com.google.android.calculator"
# Specify the Calculator app activity
options.app_activity = "com.android.calculator2.Calculator"

# Keep the app data instead of resetting it
options.no_reset = True


# Create a WebDriver session and launch the Calculator app
driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)

try:

    # Find the button using its accessibility ID
    number_five = driver.find_element(
        AppiumBy.ACCESSIBILITY_ID, "5"
    )
    number_five.click()
    time.sleep(2)

    # Get the current text displayed by the Calculator
    display = driver.find_element(
        AppiumBy.ID,
        "com.google.android.calculator:id/result_final"
    )

    displayed_value = display.text

    # Verify that the displayed value is 5
    assert displayed_value == "5", (
        f"Expected 5, but got {displayed_value}"
    )

    print("Test passed")
except:
        driver.quit()

        print("Appium session closed.")
