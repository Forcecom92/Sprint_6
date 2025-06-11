import pytest
from selenium import webdriver
from data import URL

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1296, 756)
    driver.get(URL.FIRST_PAGE)

    yield driver

    driver.quit()