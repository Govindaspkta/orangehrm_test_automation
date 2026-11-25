import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com").rstrip("/")
# Public demo credentials published on the OrangeHRM demo login page
ADMIN_USER = os.getenv("ORANGEHRM_USER", "Admin")
ADMIN_PASS = os.getenv("ORANGEHRM_PASS", "admin123")

try:
    expect.set_options(timeout=15000)
except AttributeError:  # older Playwright versions
    pass


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture
def creds():
    return {"username": ADMIN_USER, "password": ADMIN_PASS}


@pytest.fixture
def auth_page(page, base_url, creds):
    """A page that is already logged in as the demo admin."""
    from automation.helpers import login

    login(page, base_url, creds["username"], creds["password"])
    expect(page).to_have_url(f"{base_url}/web/index.php/dashboard/index")
    return page
