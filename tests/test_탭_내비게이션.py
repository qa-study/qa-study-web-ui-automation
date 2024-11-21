import elements.el_webtoon_main as element
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class 탭_내비게이션(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    def test_웹툰_탭_이동(self):
        BasePage.click_element(self, By.XPATH, element.xpath_webtoon_webtoon_tap)
