# Importing the necessary Selenium WebDriver module to control web browsers
from selenium import webdriver
# Importing specific element locating strategies from Selenium's WebDriver module
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# Creating a Login class for handling login functionality
class Logout:
    # Storing locators for elements on the login page
    text_box_username_Name = "username"  # Locator for the username text box using the 'name' attribute
    text_box_password_Name = "password"  # Locator for the password text box using the 'name' attribute
    btn_login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'  # XPath for the login button
    dropdown_menu_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li'
    btn_logout_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a'

    # Initializing the Login class with a WebDriver instance
    def __init__(self, driver):
        self.driver = driver

    # Method to set the username in the username text box
    def setUsername(self, username):
        # Finding the username element by its name, clearing any existing text, and entering the provided username
        self.driver.find_element(By.NAME, self.text_box_username_Name).clear()
        self.driver.find_element(By.NAME, self.text_box_username_Name).send_keys(username)

    # Method to set the password in the password text box
    def setPassword(self, password):
        # Finding the password element by its name, clearing any existing text, and entering the provided password
        self.driver.find_element(By.NAME, self.text_box_password_Name).clear()
        self.driver.find_element(By.NAME, self.text_box_password_Name).send_keys(password)

    # Method to perform a click action on the login button
    def clickLogin(self):
        # Locating the login button by its XPath and clicking it to initiate the login process
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def selectDropdown(self):
        self.driver.find_element(By.XPATH, self.dropdown_menu_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()
