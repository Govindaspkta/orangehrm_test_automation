import time
import pytest
from playwright.sync_api import Page, expect

MENU_ITEMS = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Directory"]


# TC_DASH_02: every left menu module opens without an error
@pytest.mark.parametrize("item", MENU_ITEMS)
def test_dash_02_menu_item_opens(auth_page: Page, item):
    auth_page.get_by_role("link", name=item, exact=True).click()
    expect(auth_page.locator(".oxd-topbar-header-breadcrumb")).to_be_visible()


# TC_DASH_03: menu search filters the left menu
def test_dash_03_menu_search(auth_page: Page):
    auth_page.get_by_placeholder("Search").fill("Leave")
    expect(auth_page.get_by_role("link", name="Leave", exact=True)).to_be_visible()
    expect(auth_page.get_by_role("link", name="Admin", exact=True)).to_be_hidden()


# TC_PIM_02: add employee with empty names shows Required
def test_pim_02_add_employee_required_names(auth_page: Page, base_url):
    auth_page.goto(f"{base_url}/web/index.php/pim/addEmployee")
    auth_page.get_by_role("button", name="Save").click()
    expect(auth_page.get_by_text("Required").first).to_be_visible()
    expect(auth_page).to_have_url(f"{base_url}/web/index.php/pim/addEmployee")


# TC_PIM_01: add an employee successfully
def test_pim_01_add_employee(auth_page: Page, base_url):
    auth_page.goto(f"{base_url}/web/index.php/pim/addEmployee")
    auth_page.locator('input[name="firstName"]').fill("Sanjay")
    auth_page.locator('input[name="lastName"]').fill(f"Thapa{int(time.time())}")
    auth_page.get_by_role("button", name="Save").click()
    expect(auth_page.get_by_text("Successfully Saved").first).to_be_visible()
    expect(auth_page.get_by_role("heading", name="Personal Details")).to_be_visible()


# TC_PIM_06: search for a name that does not exist
def test_pim_06_search_no_match(auth_page: Page, base_url):
    auth_page.goto(f"{base_url}/web/index.php/pim/viewEmployeeList")
    auth_page.get_by_placeholder("Type for hints...").first.fill("Zxqwv")
    auth_page.get_by_role("button", name="Search").click()
    expect(auth_page.get_by_text("No Records Found").first).to_be_visible()
