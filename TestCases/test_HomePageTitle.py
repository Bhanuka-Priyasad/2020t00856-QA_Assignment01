# Importing the pytest library for test framework functionalities
import pytest
# Importing the webdriver module from Selenium for browser automation
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.VerifyHomePageTitle import Title
# Importing the time module for time-related operations
import time


# Defining a test class named Test_001_Login
class Test_001_Title:
    # Declaring class-level variables for base URL, username, and password
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    # Test method to verify the home page title
    def test_LoginpageTitle(self):
        # Initiating a Chrome WebDriver instance
        self.driver = webdriver.Chrome()

        # Maximizing the browser window
        self.driver.maximize_window()

        # Navigating to the specified base URL
        self.driver.get(self.base_url)

        # Pausing execution for 5 seconds to ensure page loads completely
        time.sleep(5)

        # Getting the title of the current page
        act_title = self.driver.title

        # Closing the browser session
        self.driver.quit()

        # Checking if the actual title matches the expected title
        if act_title == "OrangeHRM":
            assert True
            print("Title matches: Test Passed")
        else:
            assert False
            print("Title doesn't match: Test Failed")


