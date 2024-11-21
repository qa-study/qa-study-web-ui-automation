from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, selector, locator):
        element = self.driver.find_element(by=selector, value=locator)
        element.click()

    def input_element(self, selector, locator, text):
        element = self.driver.find_element(by=selector, value=locator)
        element.send_keys(text)

    def is_displayed(self, selector, locator):
        element = self.driver.find_element(by=selector, value=locator)
        element.is_displayed()