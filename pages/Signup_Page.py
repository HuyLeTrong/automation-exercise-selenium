import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support import expected_conditions as EC

class SignUpPage:
    # Locators
    GENDER_MRS = (By.ID, "id_gender2")
    GENDER_MR = (By.ID, "id_gender1")
    SIGNUP_NAME= (By.ID, "name")
    SIGNUP_EMAIL = (By.ID, "email")
    SIGNUP_PASSWORD = (By.ID, "password")
    SIGNUP_BDAY = (By.ID, "days")
    SIGNUP_BMONTH = (By.ID, "months")
    SIGNUP_BYEAR = (By.ID, "years")
    SIGNUP_NEWSLETTER = (By.ID, "newsletter")
    SIGNUP_OPTIN = (By.ID, "optin")

    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    COMPANY = (By.ID, "company")
    ADDRESS  = (By.ID, "address1")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE = (By.ID, "mobile_number")
    CREATE_BUTTON   = (By.CSS_SELECTOR, 'button[data-qa="create-account"]')

    def __init__(self, driver, base_url):
        self.driver = driver
        self.wait   = WebDriverWait(driver, 10)
        self.base_url = base_url

    def visit(self):
        self.driver.get(f"{self.base_url}/signup")

    def signup_title(self):
        gender = random.choice([self.GENDER_MR, self.GENDER_MRS])
        self.wait.until(EC.element_to_be_clickable(gender)).click()

    def signup_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.SIGNUP_PASSWORD)).send_keys(password)

    def assert_signup_name_email(self, name, email):
        assert self.wait.until(EC.visibility_of_element_located(self.SIGNUP_NAME)).get_attribute("value") == name
        assert self.wait.until(EC.visibility_of_element_located(self.SIGNUP_EMAIL)).get_attribute("value") == email

    def select_dob(self, day, month, year):
        Select(self.wait.until(EC.element_to_be_clickable(self.SIGNUP_BDAY))).select_by_visible_text(day)
        Select(self.wait.until(EC.element_to_be_clickable(self.SIGNUP_BMONTH))).select_by_visible_text(month)
        Select(self.wait.until(EC.element_to_be_clickable(self.SIGNUP_BYEAR))).select_by_visible_text(year)

    def newsletter(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGNUP_NEWSLETTER)).click()

    def optin(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGNUP_OPTIN)).click()

    def fill_name(self, first_name, last_name):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first_name)
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME)).send_keys(last_name)

    def fill_personal_info(self, company, address, country, state, city, zipcode, mobile):
        self.wait.until(EC.visibility_of_element_located(self.COMPANY)).send_keys(company)
        self.wait.until(EC.visibility_of_element_located(self.ADDRESS)).send_keys(address)
        Select(self.wait.until(EC.visibility_of_element_located(self.COUNTRY))).select_by_visible_text(country)
        self.wait.until(EC.visibility_of_element_located(self.STATE)).send_keys(state)
        self.wait.until(EC.visibility_of_element_located(self.CITY)).send_keys(city)
        self.wait.until(EC.visibility_of_element_located(self.ZIPCODE)).send_keys(zipcode)
        self.wait.until(EC.visibility_of_element_located(self.MOBILE)).send_keys(mobile)

    def click_create_account(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_BUTTON)).click()
