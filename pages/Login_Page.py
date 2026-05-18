# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # Locators
    EMAIL_INPUT    = (By.CSS_SELECTOR, 'input[data-qa="login-email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[data-qa="login-password"]')
    LOGIN_BUTTON   = (By.CSS_SELECTOR, 'button[data-qa="login-button"]')
    SIGNUP_NAME    = (By.CSS_SELECTOR, 'input[data-qa="signup-name"]')
    SIGNUP_EMAIL   = (By.CSS_SELECTOR, 'input[data-qa="signup-email"]')
    SIGNUP_BUTTON  = (By.CSS_SELECTOR, 'button[data-qa="signup-button"]')
    ERROR_MESSAGE  = (By.CSS_SELECTOR, 'p[style*="color: red"]')

    def __init__(self, driver, base_url):
        self.driver = driver
        self.wait   = WebDriverWait(driver, 10)
        self.base_url = base_url

    def visit(self):
        self.driver.get(f"{self.base_url}/login")

    def signup_name(self, name):
        self.wait.until(EC.visibility_of_element_located(self.SIGNUP_NAME)).send_keys(name)

    def signup_email(self, email):
        self.wait.until(EC.visibility_of_element_located(self.SIGNUP_EMAIL)).send_keys(email)                                   

    def click_signup(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGNUP_BUTTON)).click()

    def enter_email(self, email):
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(email)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))