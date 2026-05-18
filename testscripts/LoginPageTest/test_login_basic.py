import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from testscripts.pages.Login_Page import LoginPage

def test_login_page_loads(driver, base_url):
    page = LoginPage(driver, base_url)
    page.visit()
    assert driver.current_url == f"{base_url}/login"

def test_login_page_create_account(driver, base_url):
    page = LoginPage(driver, base_url)
    page.visit()
    assert driver.current_url == f"{base_url}/login"

    page.signup_name("Tester H")
    page.signup_email("copak40626@dardr.com") #use unique email each time, generate with https://temp-mail.org/en/
    page.click_signup()

    WebDriverWait(driver, 10).until(EC.url_contains("/signup"))
    assert driver.current_url == f"{base_url}/signup"
    page.wait.until(EC.element_to_be_clickable((By.ID, "id_gender2"))).click() #Mr/Ms radio button
    page.wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("password123")

    oSelect = Select(page.wait.until(EC.visibility_of_element_located((By.ID, "days"))))
    oSelect.select_by_visible_text("7")
    oSelect = Select(page.wait.until(EC.visibility_of_element_located((By.ID, "months"))))
    oSelect.select_by_visible_text("September")
    oSelect = Select(page.wait.until(EC.visibility_of_element_located((By.ID, "years"))))
    oSelect.select_by_visible_text("1990")

    page.wait.until(EC.visibility_of_element_located((By.ID, "newsletter"))).click()
    page.wait.until(EC.visibility_of_element_located((By.ID, "optin"))).click()

    page.wait.until(EC.visibility_of_element_located((By.ID, "first_name"))).send_keys("Tester")
    page.wait.until(EC.visibility_of_element_located((By.ID, "last_name"))).send_keys("Huy")
    page.wait.until(EC.visibility_of_element_located((By.ID, "company"))).send_keys("S Tech")
    page.wait.until(EC.visibility_of_element_located((By.ID, "address1"))).send_keys("123 Main St")
    oSelectCountry = Select(page.wait.until(EC.visibility_of_element_located((By.ID, "country"))))
    oSelectCountry.select_by_visible_text("Canada")
    page.wait.until(EC.visibility_of_element_located((By.ID, "state"))).send_keys("FakeState")
    page.wait.until(EC.visibility_of_element_located((By.ID, "city"))).send_keys("FakeCity")
    page.wait.until(EC.visibility_of_element_located((By.ID, "zipcode"))).send_keys("10000")
    page.wait.until(EC.visibility_of_element_located((By.ID, "mobile_number"))).send_keys("1234567890")
    page.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="create-account"]'))).click()

    WebDriverWait(driver, 10).until(EC.url_contains("/account_created"))
    assert driver.current_url == f"{base_url}/account_created"
