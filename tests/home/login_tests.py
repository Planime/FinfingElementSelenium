import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage


class LoginTests(unittest.TestCase):

    def test_validLogin(self):

        baseUrl = "https://learn.letskodeit.com/"

        driverLocation = "/Users/artemdigtiar/Documents/Selenium/ChromeDriver/chromedriver"
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(3)

        driver.get(baseUrl)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")

        userIcon = driver.find_element(By.XPATH, '//*[@id="udemy"]/div[2]/div[2]/div[1]/div[1]/a/img')
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")


