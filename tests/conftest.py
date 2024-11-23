import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    # Chrome WebDriver 초기화
    driver = webdriver.Chrome()
    driver.get("https://comic.naver.com/index")
    driver.implicitly_wait(5)
    yield driver
