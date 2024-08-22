import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from utilities.configuration import Readconfig
from utilities.logger import loger


class Test_NewSite:
    log = loger.loggr()
    config = Readconfig

    def test_CNG(self):
        driver = webdriver.Chrome()
        driver.get("https://automation.credence.in/login")
        self.log.info("Successfully entered")
        driver.find_element(By.XPATH, "//input[@id='email']]").send_keys(self.config.getusername())
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys(self.config.getPassword())
        driver.save_screenshot("NEwlyversion\\Automation.png")
        if driver.title == 'CredKart':
            print("We succefully passed")
            assert True
        else:
            assert False

    # @pytest.mark.sanity1
    # def test_Panda(self, Set_up):
    #     driver = Set_up
    #     self.log.info("Second panda")
    #     driver.find_element(By.XPATH, "//input[@id='email']]").send_keys(self.config.getusername())
    #     driver.find_element(By.XPATH, "//input[@id='password']").send_keys(self.config.getPassword())
    #     time.sleep(5)

    @pytest.mark.sanity
    def test_Alter(self):
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click()
        time.sleep(5)
        Al=Alert(driver)
        Alert(driver).accept()
        print(driver.find_element(By.XPATH, "//p[@id='result']").text)
        Alert(driver).dismiss()
        Alert(driver).send_keys("Hi this is Nidhisha Pradip khanekar")


