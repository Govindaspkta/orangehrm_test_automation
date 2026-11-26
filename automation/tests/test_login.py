import pytest
from playwright.sync_api import Page, expect
from automation.helpers import login, LOGIN_PATH


# TC_LOGIN_01: valid login opens the dashboard
def test_login_01_valid_login(page: Page, base_url, creds):
    login(page, base_url, creds["username"], creds["password"])
    expect(page).to_have_url(f"{base_url}/web/index.php/dashboard/index")
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()


# TC_LOGIN_02: wrong password shows an error
def test_login_02_wrong_password(page: Page, base_url, creds):
    login(page, base_url, creds["username"], "admin@999")
    expect(page.locator(".oxd-alert-content-text")).to_have_text("Invalid credentials")
    expect(page).to_have_url(f"{base_url}{LOGIN_PATH}")


# TC_LOGIN_03: empty fields show Required under both inputs
def test_login_03_empty_fields(page: Page, base_url):
    page.goto(f"{base_url}{LOGIN_PATH}")
    page.locator('button[type="submit"]').click()
    errors = page.locator(".oxd-input-field-error-message")
    expect(errors).to_have_count(2)
    expect(errors.first).to_have_text("Required")


# TC_LOGIN_04: password empty shows Required under password only
def test_login_04_empty_password(page: Page, base_url, creds):
    page.goto(f"{base_url}{LOGIN_PATH}")
    page.locator('input[name="username"]').fill(creds["username"])
    page.locator('button[type="submit"]').click()
    expect(page.locator(".oxd-input-field-error-message")).to_have_count(1)


# TC_LOGIN_06: forgot password flow
def test_login_06_forgot_password(page: Page, base_url, creds):
    page.goto(f"{base_url}{LOGIN_PATH}")
    page.get_by_text("Forgot your password?").click()
    page.locator('input[name="username"]').fill(creds["username"])
    page.get_by_role("button", name="Reset Password").click()
    expect(page.get_by_text("Reset Password link sent successfully")).to_be_visible()


# TC_LOGIN_08: logout returns to the login page
def test_login_08_logout(auth_page: Page, base_url):
    auth_page.locator(".oxd-userdropdown-tab").click()
    auth_page.get_by_role("menuitem", name="Logout").click()
    expect(auth_page).to_have_url(f"{base_url}{LOGIN_PATH}")


# Protected page without login redirects to login
def test_protected_page_redirects_to_login(page: Page, base_url):
    page.goto(f"{base_url}/web/index.php/pim/viewEmployeeList")
    expect(page).to_have_url(f"{base_url}{LOGIN_PATH}")

# Data-driven: several invalid username/password combinations
@pytest.mark.parametrize("username, password", [
    ("Admin", "wrong123"),
    ("wrong", "admin123"),
    ("ADMIN", "admin@999"),
    ("wrong", "wrong"),
])
def test_invalid_login_data_driven(page: Page, base_url, username, password):
    login(page, base_url, username, password)
    expect(page.locator(".oxd-alert-content-text")).to_have_text("Invalid credentials")
    expect(page).to_have_url(f"{base_url}{LOGIN_PATH}")