from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from url import *
import pytest


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    driver = webdriver.Chrome(options=options)
    driver.get(main_site)
    yield driver
    driver.quit()
