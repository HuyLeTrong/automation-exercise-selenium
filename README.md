# Automation Exercise - Selenium Test Suite

Automated end-to-end test suite for [automationexercise.com](https://automationexercise.com) built with Selenium WebDriver, pytest, and Python. Tests run locally and automatically via GitHub Actions CI/CD on every push.

---

## Tech Stack

- **Python 3.13**
- **Selenium 4.x** — browser automation (includes Selenium Manager, no manual ChromeDriver setup needed)
- **pytest** — test runner and fixtures
- **GitHub Actions** — CI/CD pipeline

---

## Project Structure

```
automation-exercise-selenium/
├── .github/
│   └── workflows/
│       └── automation-exercise-selenium.yml  # CI/CD pipeline
├── pages/                                    # Page Object Model classes
│   ├── __init__.py
│   ├── Login_Page.py                         # Login page actions and locators
│   └── Signup_Page.py                        # Signup page actions and locators
├── testscripts/
│   └── LoginPageTest/
│       ├── __init__.py
│       └── test_login_basic.py               # Login and signup test cases
├── conftest.py                               # pytest fixtures (driver, base_url)
├── pytest.ini                                # pytest configuration
├── requirements.txt                          # project dependencies
└── README.md
```

---

## Test Cases

| Test | Description |
|---|---|
| `test_login_page_loads` | Verifies the login page loads and URL is correct |
| `test_login_page_create_account` | Full end-to-end account creation flow including form validation |

---

## Local Setup

### Prerequisites
- Python 3.13+ installed — [python.org/downloads](https://www.python.org/downloads/)
- Google Chrome installed
- PowerShell execution policy set (Windows only, run once):
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 1. Clone the repository
```bash
git clone https://github.com/HuyLeTrong/automation-exercise-selenium.git
cd automation-exercise-selenium
```

### 2. Create a virtual environment
```cmd
py -3.13 -m venv auto_exercise_env
```

### 3. Install dependencies
```cmd
auto_exercise_env\Scripts\pip.exe install -r requirements.txt
```

### 4. Run tests
```cmd
auto_exercise_env\Scripts\python.exe -m pytest testscripts/ -v
```

---

## CI/CD

Tests run automatically on every push and pull request to `main` via GitHub Actions.

The pipeline:
1. Spins up an Ubuntu runner
2. Installs Python 3.13 and dependencies from `requirements.txt`
3. Runs Chrome in headless mode (automatically detected via `CI` environment variable)
4. Reports pass/fail results in the Actions tab

Headless mode is handled automatically in `conftest.py` — no manual configuration needed between local and CI environments.

---

## Notes

- A unique email is generated per test run using a Unix timestamp to avoid duplicate account registration errors
- ChromeDriver is managed automatically by Selenium Manager — no manual driver download or version matching required
- Page Object Model (POM) pattern is used to separate locators and actions from test logic, with page chaining on navigation
