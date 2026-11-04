# Import Modules

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

@pytest.fixture()

def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"      #device name after adb devices
    options.automation_name = "UiAutomator2"   #set automation engine

    # Replace with your actual apk name
    options.app =r"C:\\Users\\rizal\\OneDrive\\Documents\\MindrisersPython\\Mobile Test - Appium\\app-release.apk"   
    #Desired Capabalities till here.

    #create drive session 4723 is port for appium server
    driver = webdriver.Remote("http://localhost:4723", options=options)
