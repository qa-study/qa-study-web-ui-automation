from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://comic.naver.com/index")
    driver.implicitly_wait(5)
    yield driver
