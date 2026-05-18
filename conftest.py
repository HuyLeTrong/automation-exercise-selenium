# conftest.py
import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://automationexercise.com"

@pytest.fixture(scope="function")
def driver():
    options = Options()
    if os.getenv("CI"):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(8)            # like defaultCommandTimeout in Cypress
    driver.maximize_window()
    yield driver
    driver.quit()                        # runs after each test, like cy.clearCookies()

@pytest.fixture(scope="function")
def base_url():
    return BASE_URL