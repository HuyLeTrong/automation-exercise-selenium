from selenium.webdriver.support.ui import WebDriverWait
import time

from selenium.webdriver.support import expected_conditions as EC

from pages.Login_Page import LoginPage

def test_login_page_loads(driver, base_url):
    page = LoginPage(driver, base_url)
    page.visit()
    assert driver.current_url == f"{base_url}/login"

def test_login_page_create_account(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.visit()
    assert driver.current_url == f"{base_url}/login"

    unique_email = f"tester_{int(time.time())}@dardr.com"
    login_page.signup_name("Tester H")
    login_page.signup_email(unique_email) #auto generate unique email to avoid email already exist.
    signup_page = login_page.click_signup()

    WebDriverWait(driver, 10).until(EC.url_contains("/signup"))
    assert driver.current_url == f"{base_url}/signup"

    signup_page.assert_signup_name_email("Tester H", unique_email)

    signup_page.signup_title()
    signup_page.signup_password("password123")

    signup_page.select_dob("10", "May", "1990")

    signup_page.newsletter()
    signup_page.optin()

    signup_page.fill_name("Tester", "Huy")
    signup_page.fill_personal_info("S Tech", "123 Main St", "Canada", "FakeState", "FakeCity", "10000", "1234567890")

    signup_page.click_create_account()


    WebDriverWait(driver, 10).until(EC.url_contains("/account_created"))
    assert driver.current_url == f"{base_url}/account_created"
