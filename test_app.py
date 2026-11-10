#import required modules
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
#create options object
options = UiAutomator2Options()

#Desired Capabilities
#platform name
options.platform_name = "Android"
options.device_name = "emulator-5554"      #device name after adb devices
options.automation_name = "UiAutomator2"   #set automation engine

# Replace with your actual apk name
options.app ="C:\\Users\\rizal\\OneDrive\\Documents\\MindrisersPython\\Mobile Test - Appium\\app-release.apk"   # Desired Capabalities till here.

#create drive session 4723 is port for appium server
driver = webdriver.Remote("http://localhost:4723", options=options)
driver.implicitly_wait(10)
time.sleep(5)
print("Your App Launched Successfully")

# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Start").click()
# time.sleep(3)
# # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)').click()
# # time.sleep(2)
# driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]").send_keys("sujan123@gmail.com")
# time.sleep(3)
# driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]").send_keys("Password@123")
# time.sleep(2)
# driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Login']").click()
# time.sleep(2)
# driver.quit()