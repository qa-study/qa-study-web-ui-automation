

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def driver_title(self, expected_title):
        actual_title = self.driver.title
        assert actual_title == expected_title

    def click_element(self, selector, locator):
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(by=selector, value=locator)
        element.click()

    def input_element(self, selector, locator, text):
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(by=selector, value=locator)
        element.send_keys(text)

    def is_displayed(self, selector, locator):
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(by=selector, value=locator)
        return element.is_displayed()