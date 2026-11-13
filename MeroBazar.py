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
print("Your App Launched Successfully")

#Performing actions
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Start").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Sign up").click()
time.sleep(2)

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)').click()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)').send_keys("Sujan Rijal")
time.sleep(3) # hardcore wait

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)').click()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)').send_keys("Sujantests@gmail.com")
time.sleep(2)

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(2)').click()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(2)').send_keys("Sujan12345")

driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Sign up").click()
time.sleep(6)

#Locating Email Field
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)').click()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)').send_keys("Sujantests@gmail.com")
time.sleep(2)

#Locating Password field
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)').click()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)').send_keys("Sujan12345")
time.sleep(3)

# Click Login
login_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Login")')
login_button.click()
time.sleep(10)
print("Login Sucessful")

